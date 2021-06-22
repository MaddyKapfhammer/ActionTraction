# from pydriller import RepositoryMining
from pydriller import Repository
from typing import List
import pandas as pd
import numpy as np
import os
import pathlib


def generate_file_list(repository_path: str):
    files_changed_list = []
    for commit in Repository(repository_path, only_modifications_with_file_types=['.yml']).traverse_commits():
        for changed_file in commit.modified_files:
            files_changed_list.append(changed_file.new_path)
    
    return files_changed_list


def determine_actions_files(modified_files: List[str]):
    files_to_analyze = []
    for file in modified_files:
        if ".github" in str(file):
            if files_to_analyze.count(str(file)) == 0:
                files_to_analyze.append(str(file))
    
    return files_to_analyze


def iterate_actions_files(repository_path: str, files_to_analyze: List[str]):
    author_list = []
    committer_list = []
    date_list = []
    branches_list = []
    commit_messages_list = []
    files_changed_list = []
    lines_added_list = []
    lines_deleted_list = []
    source_code_list = []
    file_list = []
    repository_list = []
    size_bytes_list = []
    raw_data = {}

    final_dataframe = pd.DataFrame()
    first_dataframe = pd.DataFrame()
    for file in files_to_analyze:
        for commit in Repository(repository_path, filepath=file).traverse_commits(): 
            complete_file = repository_path + "/" + file
            file_list.append(file)
            repository_list.append(repository_path)
            author_list.append(commit.author.name)
            committer_list.append(commit.committer.name)
            date_list.append(commit.committer_date)
            branches_list.append(commit.branches)
            commit_messages_list.append(commit.msg)
            size_bytes_list.append(os.stat(complete_file).st_size)
            lines_added_list.append(commit.insertions)
            lines_deleted_list.append(commit.deletions)
        raw_data["Repository"] = repository_list
        raw_data["File"] = file_list
        raw_data["File Size in Bytes"] = size_bytes_list
        raw_data["Author"] = author_list
        raw_data["Committer"] = committer_list
        raw_data["Branches"] = branches_list
        raw_data["Commit Message"] = commit_messages_list
        raw_data["Lines Added"] = lines_added_list
        raw_data["Lines Removed"] = lines_deleted_list
        raw_data["Date of Change"] = date_list

    first_dataframe = pd.DataFrame.from_dict(raw_data, orient="columns")
    
    return first_dataframe


def iterate_through_directory(root_directory: str):
    repos_to_check = []
    dataframes_list = []
    final_dataframe = pd.DataFrame()
    for subdir, dirs, files in os.walk(root_directory):
        repos_to_check.append(dirs)
    
    for repository in repos_to_check[0]:
        path = pathlib.Path.home() / root_directory / repository
        all_files_changed = generate_file_list(str(path))
        actions_files = determine_actions_files(all_files_changed)
        single_repo_dataframe = iterate_actions_files(str(path), actions_files)
        dataframes_list.append(single_repo_dataframe)
    
    for initial_data in dataframes_list:
        final_dataframe = final_dataframe.append(initial_data)
    csv_path = root_directory + "/minedRepos.csv"
    print("Repository Mining Completed")
    final_dataframe.to_csv(csv_path)