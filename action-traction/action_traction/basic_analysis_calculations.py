import statistics
import pandas as pd

def determine_repositories(initial_data):
    repository_list = initial_data["Repository"].tolist()
    repository_set = set(repository_list)
    return repository_set


def determine_files_per_repo(initial_data, repository_set):
    repo_file_dict = {}
    for repository in repository_set:
        new_data = initial_data.loc[initial_data['Repository'] == repository]
        # print(new_data)
        file_list = new_data["File"].tolist()
        file_set = set(file_list)
        repo_file_dict[repository] = file_set
    # print(repo_file_dict)
    return repo_file_dict


def calculate_size_metrics(initial_data, repo_file_dict):
    minimum = 0
    maximum = 0
    size_dictionary = {}
    final_dict = {}
    dataframe_list = []
    size_dataframe = pd.DataFrame()
    for repo, file_list in repo_file_dict.items():
        for file in file_list:
            new_data = initial_data.loc[initial_data['File'] == file]
            size_list = new_data["File Size in Bytes"].tolist()
            
            minimum = min(size_list)
            maximum = max(size_list)
            mean = statistics.mean(size_list)
            median = statistics.median(size_list)
            st_dev = statistics.stdev(size_list)
            variance = statistics.variance(size_list)
            
            size_dictionary["Repository"] = [repo]
            size_dictionary["File"] = [file]
            size_dictionary["Minimum"] = [minimum]
            size_dictionary["Maximum"] = [maximum]
            size_dictionary["Mean"] = [mean]
            size_dictionary["Median"] = [median]
            size_dictionary["Standard Deviation"] = [st_dev]
            size_dictionary["Variance"] = [variance]

            initial_size_dataframe = pd.DataFrame.from_dict(size_dictionary)
            dataframe_list.append(initial_size_dataframe)
    for result in dataframe_list:
        size_dataframe = size_dataframe.append(result)
    return size_dataframe


def calculate_author_metrics(initial_data, repo_file_dict):
    author_dictionary = {}
    count_unique_authors = 0
    dataframe_list = []
    author_dataframe = pd.DataFrame()
    for repo, file_list in repo_file_dict.items():
        for file in file_list:
            new_data = initial_data.loc[initial_data['File'] == file]
            author_list = new_data["Author"].tolist()
            author_set = set(author_list)
            list_percentage_contributions = []
            for unique_author in author_set:
                unique_author_contribution = author_list.count(unique_author)
                author_percentage_contribution = (unique_author_contribution) / len(author_list) * 100
                list_percentage_contributions.append(author_percentage_contribution)
                
                author_dictionary["Repository"] = [repo]
                author_dictionary["File"] = [file]
                author_dictionary["Author"] = [unique_author]
                author_dictionary["Number Corresponding Commits"] = unique_author_contribution
                author_dictionary["Percentage Contribution"] = [author_percentage_contribution]

                initial_dataframe = pd.DataFrame.from_dict(author_dictionary, orient="columns")
                dataframe_list.append(initial_dataframe)
    
    for result in dataframe_list:
        author_dataframe = author_dataframe.append(result)

    return author_dataframe


def calculate_committer_metrics(initial_data, repo_file_dict):
    committer_dictionary = {}
    count_unique_committer = 0
    dataframe_list = []
    committer_dataframe = pd.DataFrame()
    for repo, file_list in repo_file_dict.items():
        for file in file_list:
            new_data = initial_data.loc[initial_data['File'] == file]
            committer_list = new_data["Committer"].tolist()
            committer_set = set(committer_list)
            list_percentage_contributions = []
            for unique_committer in committer_set:
                unique_committer_contribution = committer_list.count(unique_committer)
                committer_percentage_contribution = (unique_committer_contribution) / len(committer_list) * 100
                list_percentage_contributions.append(committer_percentage_contribution)
                
                author_dictionary["Repository"] = [repo]
                author_dictionary["File"] = [file]
                author_dictionary["Author"] = [unique_committer]
                author_dictionary["Number Corresponding Commits"] = unique_committer_contribution
                author_dictionary["Percentage Contribution"] = [committer_percentage_contribution]
                initial_dataframe = pd.DataFrame.from_dict(committer_dictionary, orient="columns")
                dataframe_list.append(initial_dataframe)
    
    for result in dataframe_list:
        committer_dataframe = committer_dataframe.append(result)

    return committer_dataframe
    

# def calculate_branches_metrics(initial_data):
#     branches_dictionary = {}
#     branches_list = initial_data["Branches"].tolist()
#     for branch in branches_list:
#         print(type(branch))

def calculate_lines_added_metrics(initial_data, repo_file_dict):
    added_dictionary = {}
    dataframe_list = []
    added_dataframe = pd.DataFrame()
    for repo, file_list in repo_file_dict.items():
        for file in file_list:
            new_data = initial_data.loc[initial_data['File'] == file]
            lines_added_list = new_data["Lines Added"].tolist()

            mean = statistics.mean(lines_added_list)
            median = statistics.median(lines_added_list)
            minimum = min(lines_added_list)
            maximum = max(lines_added_list)
            st_dev = statistics.stdev(lines_added_list)
            variance = statistics.variance(lines_added_list)

            added_dictionary["Repository"] = [repo]
            added_dictionary["File"] = [file]
            added_dictionary["Minimum"] = [minimum]
            added_dictionary["Maximum"] = [maximum]
            added_dictionary["Mean"] = [mean]
            added_dictionary["Median"] = [median]
            added_dictionary["Standard Deviation"] = [st_dev]
            added_dictionary["Variance"] = [variance]

            initial_size_dataframe = pd.DataFrame.from_dict(added_dictionary)
            dataframe_list.append(initial_size_dataframe)

    for result in dataframe_list:
        added_dataframe = added_dataframe.append(result)
    return added_dataframe

def calculate_lines_removed_metrics(initial_data, repo_file_dict):
    removed_dictionary = {}
    dataframe_list = []
    removed_dataframe = pd.DataFrame()
    for repo, file_list in repo_file_dict.items():
        for file in file_list:
            new_data = initial_data.loc[initial_data['File'] == file]
            lines_removed_list = new_data["Lines Removed"].tolist()

            mean = statistics.mean(lines_removed_list)
            median = statistics.median(lines_removed_list)
            minimum = min(lines_removed_list)
            maximum = max(lines_removed_list)
            st_dev = statistics.stdev(lines_removed_list)
            variance = statistics.variance(lines_removed_list)

            removed_dictionary["Repository"] = [repo]
            removed_dictionary["File"] = [file]
            removed_dictionary["Minimum"] = [minimum]
            removed_dictionary["Maximum"] = [maximum]
            removed_dictionary["Mean"] = [mean]
            removed_dictionary["Median"] = [median]
            removed_dictionary["Standard Deviation"] = [st_dev]
            removed_dictionary["Variance"] = [variance]

            initial_size_dataframe = pd.DataFrame.from_dict(removed_dictionary)
            dataframe_list.append(initial_size_dataframe)

    for result in dataframe_list:
        removed_dataframe = removed_dataframe.append(result)

    return removed_dataframe


def perform_specified_summarization(specified_metrics, initial_data):
    if "Modifiers" in specified_metrics:
        author_results = calculate_author_metrics(initial_data)
        committer_results = calculate_committer_metrics(initial_data)
        print(author_results)
        print(committer_results)
    if "Size" in specified_metrics:
        size_results = calculate_size_metrics(initial_data)
        print(size_results)
    # if "Lifetime" in specified_metrics:
    #     lifetime_results = calculate_lifetime_metrics(initial_data)
    # if "Diff" in specified_metrics:
    #     added_results = calculate_lines_added_metrics(initial_data)
    #     removed_results = calculate_lines_removed_metrics(initial_data)
    #     print(added_results)
    #     print(removed_results)