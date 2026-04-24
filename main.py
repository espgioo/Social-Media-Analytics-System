# Giovanni Espindola Gonzalez
# CS302 Program 5
# Main driver file

from bst import BST
from social import Instagram, TikTok, Reddit


def main():
    tree = BST()

    while True:
        print("\nMAIN MENU")
        print("1. Add account")
        print("2. Display all accounts")
        print("3. Go to account")
        print("4. Remove account")
        print("5. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input!")
            continue

        try:
            if choice == 1:
                name = input("Enter username: ")

                print("\nSelect platform:")
                print("1. Instagram")
                print("2. TikTok")
                print("3. Reddit")

                platform = int(input("Choice: "))

                followers = int(input("Followers: "))
                posts = int(input("Posts: "))

                if platform == 1:
                    likes = int(input("Total likes: "))
                    reposts = int(input("Total reposts: "))
                    account = Instagram(name, followers, posts, likes, reposts)

                elif platform == 2:
                    comments = int(input("Total comments: "))
                    views = int(input("Total views: "))
                    account = TikTok(name, followers, posts, comments, views)

                elif platform == 3:
                    upvotes = int(input("Total upvotes: "))
                    downvotes = int(input("Total downvotes: "))
                    account = Reddit(name, followers, posts, upvotes, downvotes)

                else:
                    print("Invalid platform!")
                    continue

                tree.find_dupe(name)  # throws if duplicate
                tree.insert_node(account, platform)
                print("Account added!")

            elif choice == 2:
                tree.display()

            elif choice == 3:
                name = input("Enter username: ")
                tree.direct_to_social_menus(name)

            elif choice == 4:
                name = input("Enter username to remove: ")
                tree.remove_account(name)
                print("Account removed!")

            elif choice == 5:
                print("Exiting...")
                break

            else:
                print("Invalid option!")

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()