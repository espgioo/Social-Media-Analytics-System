# Giovanni Espindola Gonzalez - 977879121 - giovanne@pdx.edu
# CS302 Program 5
# Recovered/reconstructed BST class.

class Node:
    def __init__(self, data, choice: int):
        self._data = data
        self._left = None
        self._right = None
        self._social_type = choice

    def get_right(self): return self._right
    def get_social_data(self): return self._data
    def get_social_type(self): return self._social_type
    def get_left(self): return self._left
    def set_right(self, right): self._right = right
    def set_left(self, left): self._left = left


class BST:
    def __init__(self): self._root = None

    def insert_node(self, toAdd, choice: int):
        if self._root is None:
            self._root = Node(toAdd, choice)
            return self._root
        self._root = self.inserting_node(self._root, toAdd, choice)
        return self._root

    def inserting_node(self, root, toAdd, choice):
        if root is None: return Node(toAdd, choice)
        if root.get_social_data().get_name() > toAdd.get_name():
            root._left = self.inserting_node(root.get_left(), toAdd, choice)
        else:
            root._right = self.inserting_node(root.get_right(), toAdd, choice)
        return root

    def display(self):
        if self._root is None: raise ValueError("No accounts made! Add accounts to use!")
        return self.displaying(self._root)

    def displaying(self, root):
        if root is None: return 0
        self.displaying(root.get_left())
        print(f"Username: {root.get_social_data().get_name()}")
        self.displaying(root.get_right())
        return 0

    def retrieve(self, name):
        if self._root is None: raise ValueError("No accounts made! Add accounts to use!")
        account = self.retrieving(self._root, name)
        if account is None: raise ValueError(f"User '{name}' NOT found!")
        return account

    def retrieving(self, root, name):
        if root is None: return None
        if root.get_social_data().get_name() == name:
            print(f"Going to {name}'s account!")
            #print(root.get_social_data())
            return root
        if root.get_social_data().get_name() > name:
            return self.retrieving(root.get_left(), name)
        return self.retrieving(root.get_right(), name)

    def find_dupe(self, name):
        if self.retrieving(self._root, name) is None: return True
        raise ValueError("Username already taken!")

    def remove_account(self, name):
        if self._root is None: raise ValueError("No accounts made! Add accounts to use function!")
        self._root = self._remove_account(self._root, name)
        return self._root

    def _remove_account(self, root, name: str):
        if root is None: raise ValueError(f"User '{name}' NOT found!")
        if root.get_social_data().get_name() == name:
            if not root.get_left() and not root.get_right(): return None
            if root.get_left() and not root.get_right(): return root.get_left()
            if not root.get_left() and root.get_right(): return root.get_right()
            ios = self.find_IOS(root.get_right())
            root._data = ios.get_social_data()
            root._social_type = ios.get_social_type()
            root._right = self._remove_account(root.get_right(), ios.get_social_data().get_name())
            return root
        if root.get_social_data().get_name() > name:
            root._left = self._remove_account(root.get_left(), name)
        else:
            root._right = self._remove_account(root.get_right(), name)
        return root

    def find_IOS(self, root):
        if not root.get_left(): return root
        return self.find_IOS(root.get_left())

    def direct_to_social_menus(self, name):
        user = self.retrieve(name) #returns node
        social_type = user.get_social_type()
        if social_type == 1: self.Instagram_menu(user.get_social_data())
        elif social_type == 2: self.TikTok_menu(user.get_social_data())
        else: self.Reddit_menu(user.get_social_data())
        return self._root

    def Instagram_menu(self, user):
        print(f"Welcome to the instagram analytics page {user.get_name()}!")
        menu_choice = 0
        while menu_choice != 7:
            print("\nINSTAGRAM MENU")
            print("1. Promote account\n2. Create post\n3. Average likes per post")
            print("4. Repost Rate\n5. Engagement Rate\n6. Display all info")
            print("7. Return to main menu")
            try: menu_choice = int(input("Enter menu choice: "))
            except ValueError:
                print("Invalid input! Please enter a VALID number!\n"); continue
            try:
                if menu_choice == 1: user.promote_account()
                elif menu_choice == 2:
                    name = user.create_name("What is the name of you post?: "); user.create_Instagram_post(name)
                elif menu_choice == 3: user.avg_likes_per_post()
                elif menu_choice == 4: user.repost_rate()
                elif menu_choice == 5: user.engagement_rate()
                elif menu_choice == 6: print(user)
                elif menu_choice == 7: print("Going back to main menu..")
                elif menu_choice < 1 or menu_choice > 7: print("Invalid option. Enter a VALID menu choice!.")
            except (ValueError, ZeroDivisionError) as e: print(e)
        return user

    def TikTok_menu(self, user):
        print(f"Welcome to the TikTok analytics page {user.get_name()}!")
        menu_choice = 0
        while menu_choice != 7:
            print("\nTIKTOK MENU")
            print("1. Promote account\n2. Create post\n3. Comment-View Conversion Rate")
            print("4. Average Comment Per Post\n5. Promote video\n6. Display all account info")
            print("7. Return to main menu")
            try: menu_choice = int(input("Enter menu choice: "))
            except ValueError:
                print("Invalid input! Please enter a VALID number!\n"); continue
            try:
                if menu_choice == 1: user.promote_account()
                elif menu_choice == 2:
                    name = user.create_name("Post name: "); user.create_TikTok_post(name)
                elif menu_choice == 3: user.comment_view_conversion_rate()
                elif menu_choice == 4: user.avg_comment_per_post()
                elif menu_choice == 5:
                    user.display_posts(); name = user.create_name("What post do you want to promote?: "); index = user.find_post(name); user.viral_video(index)
                elif menu_choice == 6: print(user)
                elif menu_choice == 7: print("Going back to main menu..")
                elif menu_choice < 1 or menu_choice > 7: print("Invalid option. Enter a VALID menu choice!.")
            except (ValueError, ZeroDivisionError) as e: print(e)
        return user

    def Reddit_menu(self, user):
        print(f"Welcome to the Reddit analytics page {user.get_name()}!")
        menu_choice = 0
        while menu_choice != 7:
            print("\nREDDIT MENU")
            print("1. Promote account\n2. Create post\n3. Total account Karma")
            print("4. Average upvotes Per Post\n5. Upvote Ratio\n6. Display all account info")
            print("7. Return to main menu")
            try: menu_choice = int(input("Enter menu choice: "))
            except ValueError:
                print("Invalid input! Please enter a VALID number!\n"); continue
            try:
                if menu_choice == 1: user.promote_account()
                elif menu_choice == 2:
                    name = user.create_name("Post name: "); user.create_reddit_post(name)
                elif menu_choice == 3: user.tot_karma()
                elif menu_choice == 4: user.average_upvotes()
                elif menu_choice == 5: user.upvote_ratio()
                elif menu_choice == 6: print(user)
                elif menu_choice == 7: print("Going back to main menu..")
                elif menu_choice < 1 or menu_choice > 7: print("Invalid option. Enter a VALID menu choice!.")
            except (ValueError, ZeroDivisionError) as e: print(e)
        return user

