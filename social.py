import random

class Social:
    #type hinting, expecting a str and int
    def __init__(self, username: str, num_followers: int, posts: int):
        #_ for protected, members are declared in the constructor
        if not username:
            raise ValueError("Username cannot be empty")
        if num_followers < 0:
            raise ValueError("Followers has to be greater than 0!")

        self._username = username
        self._num_followers = num_followers
        self._num_posts = posts
        #array of posts stored as a dictionary
        self._posts = []


    #generates random followers and adds it to tot_followers
    #can possibly use op overloading here!!
    def promote_account(self):
        num = random.randint(1,100)
        self._num_followers += num
        print(f"Account has reached {num} new people!")
        print(f"Updated followers: {self._num_followers}")
        return num


    #Adds post into array of posts
    #returns a bool if adding was succesfull
    def add_post(self, post) -> bool:
        self._posts.append(post)
        return True

    #returning -1 indicates that the post does NOT exist. 
    def findPost(self, name:str) -> int:
        i = 0
        for post in self._posts:
            for key, value in post.items():
                if(value == name):
                    return i
            i += 1
        return -1


    def display(self)-> None:
        print(f"Username: {self._username}")
        print(f"Followers: {self._num_followers}")

    #Displays posts with associated key to make it generic for all classes
    def display_posts(self):
        i = 1
        for post in self._posts:
            print(f"Post number: {i}")
            for key, value in post.items():
                print(f"{key}: {value}")
            i += 1
            print()


    
#same as class Instagram: public Social{}
class Instagram(Social):
    def __init__(self, username: str, num_followers: int, posts: int, likes: int, reposts: int):
        super().__init__(username, num_followers, posts)

        self._tot_likes = likes
        self._tot_reposts = reposts


    #Calls parent's display then goes into for insta account
    def display(self)-> None:
        super().display()
        print(f"Total likes: {self._tot_likes}")
        print(f"Total reposts: {self._tot_reposts}")

    #creates post using random generated likes and reposts
    #stores into a
    def create_post(self, name: str)-> bool:

        likes: int = random.randint(1,100)
        reposts: int = random.randint(1,100)
        name: str = name
        post = {
            "name": name,
            "likes": likes,
            "reposts": reposts
        }
        super().add_post(post)
        self._tot_likes += likes
        self._tot_reposts += reposts
        self._num_posts += 1
        print(f"Your new post generated {likes} likes and {reposts} reposts")
        return True

     
    #function returns average likes per post
    def avg_likes_per_post(self) -> float:
        if self._num_posts <= 0:
            #throw exception if no posts! can't divide by 0
            raise ZeroDivisionError("Add a post to use function!")

        average: float = self._tot_likes / self._num_posts
        average = float(f"{average:.2f}")
        print(f"You average {average} likes per post!")
        #returns a float with average fixed to 2 decimals
        return average


    #Multiplies 
    def repost_rate(self) -> float:
        if self._num_followers <= 0:
            #throw exception if no posts! can't divide by 0
            raise ZeroDivisionError("No followers! Promote your account to recieve stats!") 
        rate: float = self._tot_reposts / self._num_followers
        rate *= 100
        rate = float(f"{rate:.2f}")
        print(f"Your account has an average repost rate of {rate}%!")
        return rate


    #Uses the total number of likes divided by the followers * number of posts 
    #to find the engagement rate!
    def engagement_rate(self) -> float:
        if self._num_followers <= 0:
            raise ZeroDivisionError("No followers! Promote your account to recieve stats!")
        if self._num_posts <= 0:
            raise ZeroDivisionError("No posts found! Make a new post to recieve stats!")
        engagement: float = self._tot_likes / (self._num_followers * self._num_posts)
        engagement *= 100
        engagement = float(f"{engagement:.2f}")
        print(f"Your account has an engagement rate of {engagement}%") 
        return engagement
    




#same as class Tiktok: public Social{}
class TikTok(Social):
    def __init__(self, username: str, num_followers: int, posts: int, comments: int, views: int):
        super().__init__(username, num_followers, posts)

        self._tot_comments = comments
        self._tot_views = views



    def display(self):
        super().display()
        print(f"Total comments: {self._tot_comments}")
        print(f"Total views: {self._tot_views}")


    def create_TikTok_post(self, name):
        if name == "":
            raise ValueError("Post name cannot be empty")
        
        #if name.l


        comments = random.randint(1,100)
        views = random.randint(1,100)
        name = name
        post = {
            "Post name": name,
            "Number of comments": comments,
            "Number of Views": views

        }
        super().add_post(post)
        self._tot_comments += comments
        self._tot_views += views
        self._num_posts += 1
        print(f"Your new post generated {views} views and {comments} comments")
        return post


    def comment_view_conversion_rate(self):
        if self._tot_views <= 0:
            raise ZeroDivisionError("Your account has no views! Create a new post to recieve stats!")
        rate: float = self._tot_comments / self._tot_views
        rate *= 100
        print(f"Your comment to view conversion rate is {rate:.2f}%!")
        return rate


    def avg_comment_per_post(self):
        if self._num_posts <= 0:
            raise ZeroDivisionError("Your account has no posts! Create a new post to recieve stats!")
        avg: float = self._tot_comments / self._num_posts
        print(f"You average {avg:.1f} comments per post!")
        return avg 



    #User picks a video they have posted to hit the algorithim
    #raises if not found. else, boosts comments and views!
    #updates views at that particular post
    #This is going to the index number and accesing the value
    #of comments using the "# of comments key"
    def viral_video(self, index: int):
        #picks random celeb to "promote" video 
        celeb_list = ["Daniel Caeser", "Travis Scott", "The Marias"]
        celeb = random.choice(celeb_list)

        new_views: int = random.randint(1000,100000) 
        self._posts[index]["Number of Views"] += new_views
        self._tot_views += new_views

        new_comments: int = random.randint(1,500)
       
        self._posts[index]["Number of comments"] += new_comments
        #updates total number of views from the ACCOUNT next
        self._tot_comments += new_comments
        print(f"{celeb} reposted your {self._posts[index]["Post name"]} video! Comments & view skyrocketed!")
        print(f"Current views: {self._posts[index]["Number of Views"]}")
        print(f"Current comments: {self._posts[index]["Number of comments"]}")
        return index

    

class Reddit(Social):

    def __init__(self, username: str, num_followers: int, posts: int, upvote, downvote: int):
        super().__init__(username, num_followers, posts)
        self._tot_upvote = upvote
        self._tot_downvote = downvote


    def create_reddit_post(self) -> bool:
        #this ensures a valid name is made!
        post_name = create_name("Enter post name: ")
        upvote = random.randint(1,100)
        downvote = random.randint(1,100)
        post = {
            "Post name": post_name, 
            "Number of upvotes": upvote, 
            "Number of downvote": downvote
        }
        super().add_post(post)
        self._tot_upvote += upvote
        self._tot_downvote += downvote
        self._num_posts += 1
        print(f"Your new post generated {upvote} upvotes and {downvote} downvotes")
        return True


    def tot_karma(self):
        if self._tot_upvote <= 0 or self._tot_downvote <= 0:
            raise ZeroDivisionError("Your account has no posts! Create a new post to recieve stats!") 
        acc_karma: int = self._tot_upvote - self._tot_downvote
        print(f"Your total karma for your account is {acc_karma}!")
        return acc_karma



    def average_upvotes(self):
        if self._num_posts <= 0:
            raise ZeroDivisionError("Your account has no posts! Create a new post to recieve stats!") 
        avg = self._tot_upvote / self._num_posts
        print(f"You averaged {avg} upvotes per post!")
        return avg


    def upvote_ratio(self) -> float:
        if self._tot_upvote <= 0 or self._tot_downvote <= 0:
            raise ZeroDivisionError("Your account has no posts! Create a new post to recieve stats!") 
        tot_votes = self._tot_upvote + self._tot_downvote
        #check if votes is == to 0 to prevent divide by zero
        ratio = self._tot_upvote / tot_votes
        print(f"Your account upvote ratio is {ratio}")
        return float(f"{ratio:.2f}")


    

    

# class Marketplace(Social):

#     def __init__(self, username: str, num_followers: int, posts: int, cost: float, sold: int):
#         super().__init__(username, num_followers, posts)
#         self._listing_price = cost
#         self._num_sold = sold
#         self._tot_profit = profit



#     def display(self):
#         #Check if there are posts, if no posts, raise error!!
#         super().display()
#         print(f"Item cost: ${self._cost:.2f}")
#         print(f"Sold: {self._active}")



#     def sell_post_ratio(self):
#         avg: float = self._num_sold / self._num_posts
#         avg *= 100
#         print(f"Your number of sells to post ratio is {avg:.2f}%!")
#         return avg

    
#     def sellItem(self):
#         #Prompts what post
#         print(f"What post tare you tryna sell ")
#         sellPrice = float(input("How much did you sell it for"))
#         profit: float = self

# place = Marketplace("Ssirski", 100, 10, 0, 0)
#     place.display()
#     place.sell_post_ratio()