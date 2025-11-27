from social import Instagram, TikTok, Reddit

#using this function to try out exception handiling in python
#Key notes, can pass the message as a e to then print
def create_name(prompt: str) -> str:
    name: str = ""
    while True: 
        try:
            name = input(prompt)
            if name.strip() == "":
                raise ValueError("Input cannot be empty!")
            
            else:
                #returns name if exception isn't raised!
                return name

        except ValueError as e:
            print(e)


def main():

    name = create_name("Enter your username: ")
    acc = Instagram(name, 0, 0, 0, 0)
    acc.display()

    acc.promote_account()
    

    post_name = create_name("Enter post name: ")
    
    acc.create_post(post_name)
    acc.display()

    # acc.engagement_rate()

   
    # #acc.display_posts()
    # acc.repost_rate()
   

if __name__ == '__main__':
    main()



    
   
   

    # tok = TikTok("Tammy", 222, 3, 6, 5)
    # tok.display()
    # tok.create_TikTok_post("Rocks")
    # tok.create_TikTok_post("Surfing")
    # tok.create_TikTok_post("Mountain")
    # tok.display_posts()
    # tok.comment_view_conversion_rate()
    # index = tok.findPost("Mountain")
    # tok.avg_comment_per_post()
    # tok.viral_video(index)
    # tok.display_posts()

    # acc = Reddit("GIOISCOOL", 10, 1, 22, 10)
    # acc.tot_karma()
    # acc.create_reddit_post("Cool o nah")
    # acc.average_upvotes()
    # acc.upvote_ratio()
    




 # menu_choice: int = 0
    # print("Welcome to the Social Media analytics website!")
    # while(menu_choice != 3):
    #     print("MAIN MENU")
    #     print("1. Add account\n2. Check account analytics\n3. Exit Program")
    #     try:
    #         menu_choice = int(input("Enter menu choice: "))
    #     except ValueError:
    #         print("Invalid input! Please enter a VALID number!\n")

    #     if menu_choice == 1:
    # choice: int = int(input("What type of account would you like to make?"))
    #         print("You chose: Add account")
    #         # TODO: call your add_account() function here

    #     elif menu_choice == 2:
    #         print("You chose: Check account analytics")
    #         # TODO: call your analytics() function here

    #     elif menu_choice == 3:
    #         print("Exiting program...")

    #     elif menu_choice >= 0 or menu_choice > 3:
    #         print("Invalid option. Enter a VALID menu choice!.")

    #     print()



#Make a display for the tree which only prints username
#Prompt users which acc they'll like to access 

# try:
#         acc.avg_likes_per_post()
#     except ZeroDivisionError as e:
#             print(e)
#Make a big for loop when inside the object you want to work with, Instagram, 



#When prompting users what acc they want to work with, it will be important to note
#what type of account they are to promptly bring them to the right menu functions