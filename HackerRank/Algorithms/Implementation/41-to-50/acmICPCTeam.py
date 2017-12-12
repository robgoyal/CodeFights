# Name: acmICPCTeam.py
# Author: Robin Goyal
# Last-Modified: December 12, 2017
# Purpose: Find the number of maximum topics that a team (2 attendants) knows


def acmICPCTeam(n, m, topics):
    '''
    n -> int: number of attendants to ACM ICPC
    m -> int: number of topics
    topics -> list: a string of length m with 0's and 1's where 1 represents knowledge of a specific topic

    return -> int, int: first value represents maximum number of topics a team of two knows
                        second value represents number of teams who meet the number of topics

    Each element in the topics list represents an attendants knowledge of specific topics. Find the number
    of maximum topics that a team (2 attendants) knows.

    Example:
        - topics[0] = "10101" -> attendant 1
        - topics[1] = "11001" -> attendant 2
            - The combined knowledge for both attendants is 4 topics
    '''

    max_topics = 0
    max_teams = 0

    for attendant_1 in range(n):

        # Begin at attendant_1 + 1, to avoid duplicate pairs and same attendants
        for attendant_2 in range(attendant_1 + 1, n):

            # Count number of topics if two attendants on a team would know
            team_topics = 0
            for i in range(m):
                if topics[attendant_1][i] == '1' or topics[attendant_2][i] == '1':
                    team_topics += 1

            # Update max number of topics and reinitialize number of teams who know max topics to 0
            if team_topics > max_topics:
                max_topics = team_topics
                max_teams = 1

            # Increment number of teams know the maximum number of topics
            elif team_topics == max_topics:
                max_teams += 1

    return max_topics, max_teams


def main():
    n, m = [int(i) for i in input().strip().split()]
    topics = []
    for topic in range(n):
        topic.append(str(input().strip()))

    max_topics, max_teams = acmICPCTeam(n, m, topics)
    print("{}\n{}".format(max_topics, teams))


if __name__ == "__main__":
    main()
