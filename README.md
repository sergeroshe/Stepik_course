0. Switch to main branch and do git-pull (Update)

1. Create branch
Name: feature/<chapter_num>/<sub-chapter-num>/<ex. num>_<task_name>
e.g. feature/4/3/5_check_number
Notes:
a. DO NOT USE capital letters
b. use undrscore between words

2. Create initial commit (empty main)
    def main():
      pass

    main()


3. Create the corresponding Pull Request (PR):
Name: <sub-chapter-num>_<ex. num>_<task_name> 
e.g. 4_3_5 Check Number

Notes:
a. Use regular text: spaces, capital letters, e.g.
b. Pull request should be in draft status

4. Do development with regular commits and pushes
5. Promote Pull Request to OPEN status on completion of development
   So that Vlad can review and ultimately approve it
6. Make Vlad reviewer 
7. Fix all comments in Pull Request

8. Merge approved Pull Request (PR) to main

9. Switch to main
10. Delete local feature branch
11. Git pull/update main
