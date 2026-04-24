#This is my pytest suite where I test my core heiarchy 
import pytest
from social import Social, Instagram, TikTok, Reddit

#runs test_social_display with all these different inputs
@pytest.mark.parametrize(
    "username, followers, posts",
    [
        ("Gio", 0, 1),
        ("Tammy", 10, 1),
        ("Gio2", 100, 1),
    ],
)
def test_social_display_variants(username, followers, posts, capsys):
    s = Social(username, followers, posts)

    s.display()
    #capsys.readouterror() returns everything printed so far
    #including error messsages
    captured = capsys.readouterr()

    expected = f"Username: {username}\nFollowers: {followers}\n"
    #Checks only the .out (no error messages) to above line
    assert captured.out == expected

def test_social_init():
    test = Social("Guiller", 10, 100)
    assert test._username == "Guiller"
    assert test._num_followers == 10
    assert test._num_posts == 100


#These tests are meant to catch the invalid input!
#User will NOT be allowed to adjust reposts so no need to test for that
def test_social_invalid_input_raises():
    #test "passes" if ValueError is raised, indicating the empty string was caught!
    with pytest.raises(ValueError, match="Username cannot be empty"):
        Social("", 10, 0)
        #Ditto but with negative numbers!
    with pytest.raises(ValueError, match="Followers has to be greater than 0!"):
        Social("IsThisWorking?", -20, 0) 



#Test ensures that promote Account function only gives a number >= 1
#since it's randomized, as long as it's >= 1 it's good!
def test_promote_account_function():
    s = Social("Gio", 20, 0)
    gained = s.promote_account()
    assert gained >= 1


#Dummy social in order to check the name input works since its a class mem func
def test_check_name_input():
    test = Social("DUMMY", 1, 1)
    assert test.check_name_input("WHAT") == "WHAT"

#Dummy social in order to check the name input works since its a class mem func
def test_check_name_input_too_little_chars():
    test = Social("DUMMY", 1, 1)
    with pytest.raises(ValueError):
        test.check_name_input("NO")


def test_check_name_input_too_many_chars():
    test = Social("DUMMY", 1, 1)
    with pytest.raises(ValueError):
        test.check_name_input("THISISTOMANYCHARACTERS")


def test_add_post():
    test = Social("Pewdiepie", 1, 1)
    post = {
        "name": "PEWDS",
        "Followers": 1,
        "Posts": 1
    }

    assert test.add_post(post) == True



#INSTA TESTS

#def __init__(self, username: str, num_followers: int, posts: int likes: int, reposts: int):
def test_insta_init():
    test = Instagram("Ramiro", 1, 2, 3, 4)
    assert test._username == "Ramiro"
    assert test._num_followers == 1
    assert test._num_posts == 2
    assert test._tot_likes == 3
    assert test._tot_reposts == 4


def test_Instagram_display(capfd):
    test = Instagram("Gir", 1,1,1,1)
    test.display()

    # Capture printed output
    out, err = capfd.readouterr()

    # Check expected strings
    assert "Username: Gir" in out
    assert "Followers: 1" in out
    assert "Total likes: 1" in out
    assert "Total reposts: 1" in out



def test_avg_likes_per_post():
    s = Instagram("Gio", 100, 3, 300, 2)

    #Makes sure either an int or float
    assert isinstance(s.avg_likes_per_post(), (int, float))
    #divides 300/3 == 100
    assert s.avg_likes_per_post() == 100


#Covers when no posts are  (Divide by 0)
def test_avg_likes_zero_posts_raises():
    with pytest.raises(ZeroDivisionError):
        s = Instagram("Gio", 100, 0, 0, 0)
        s.avg_likes_per_post()


#def __init__(self, username: str, num_followers: int, posts: int likes: int, reposts: int):
def test_repost_rate():
    s = Instagram("Gio", 100, 3, 300, 2)

    #Makes sure either an int or float
    assert isinstance(s.repost_rate(), (int, float))

    #divides (reposts / followers) * 100 
    assert s.repost_rate() == 2

def test_repost_rate_no_reposts():
    t2 = Instagram("Gio", 10, 3, 300, 0)
    #Makes sure either an int or float
    assert isinstance(t2.repost_rate(), (int, float))
    #when reposts is 0 and followers >= 1
    assert t2.repost_rate() == 0



#Covers when no posts are made  (Divide by 0)
def test_respost_rate_zero_followers():
    with pytest.raises(ZeroDivisionError):
        noFollowers = Instagram("Gio", 0, 0, 0, 10)
        noFollowers.repost_rate()


def test_find_post():
    s = Instagram("SZA", 1, 1, 2, 2)
    s.create_Instagram_post("GIO")
    #Should return 0 indicating first one on array
    assert s.find_post("GIO") == 0



def test_engagement_rate():
    s = Instagram("LIL YATCHY", 1, 5, 10, 5)
    assert s.engagement_rate() == 200


#Makes sure engagement rate raises error when 0 followers
def test_engagement_rate_no_followers():
    s = Instagram("LIL YATCHY", 0, 5, 10, 5)
    with pytest.raises(ZeroDivisionError):
        s.engagement_rate()


#Makes sure engagement rate raises error when 0 posts
def test_engagement_rate_no_posts():
    s = Instagram("LIL YATCHY", 10, 0, 10, 5)
    with pytest.raises(ZeroDivisionError):
        s.engagement_rate()



#Goes through list and will raise value if name is NOT found
def test_find_post_post_name_does_not_exist():
    s = Instagram("SZA", 1, 1, 2, 2)
    s.create_Instagram_post("GIO")
    with pytest.raises(ValueError):
        s.find_post("NOTFOUND")


#Creates new IG post and asserts all members are greater than intial contructor
#values
def test_create_Instagram_post():
    test = Instagram("Pewdiepie", 1, 1, 1, 1)

    assert test.create_Instagram_post("NEW GAME") == True
    assert test._tot_likes > 1
    assert test._tot_reposts > 1
    assert test._num_posts > 1


def test_create_post_too_little_chars():
    t = Instagram("Pewdiepie", 1, 1, 1, 1)

    with pytest.raises(ValueError):
        t.create_Instagram_post("")




########TIKTOK TESTS#######
def test_tiktok_init():
    test = TikTok("Ramiro", 1, 2, 3, 4)
    assert test._username == "Ramiro"
    assert test._num_followers == 1
    assert test._num_posts == 2
    assert test._tot_comments == 3
    assert test._tot_views == 4


def test_TikTok_display(capfd):
    test = TikTok("Darwin", 1,1,1,1)
    test.display()

    # Capture printed output
    out, err = capfd.readouterr()

    # Check expected strings
    assert "Username: Darwin" in out
    assert "Followers: 1" in out
    assert "Total comments: 1" in out
    assert "Total views: 1" in out



def test_comment_view_conversion_rate():
    t = TikTok("Ramiro", 22, 1, 30, 60)
    
    assert isinstance(t.comment_view_conversion_rate(), (int, float))
    #testing 30/60 == .5 * 100
    assert t.comment_view_conversion_rate() == 50



def test_comment_view_conversion_rate_no_views():
    t = TikTok("Lucas", 1, 1, 1, 0)
    with pytest.raises(ZeroDivisionError):
        t.comment_view_conversion_rate() 


def test_avg_comment_per_post():
    tik = TikTok("Vere", 1, 20, 100, 1)

    assert isinstance(tik.avg_comment_per_post(), (int, float))
    #testing 100/20 == 5
    assert tik.avg_comment_per_post() == 5


def test_avg_comment_per_post_no_posts():
    #no posts means no comments or views!
    tik = TikTok("Don Toliver", 1, 0, 0, 0)
    with pytest.raises(ZeroDivisionError):
        tik.avg_comment_per_post()



#This function makes sure a valid post is found in order to run!
#Meaning, it will NOT run if the post name user entered is NOT found!
def test_viral_video():
    tok = TikTok("Lucas", 1, 1, 1, 1)
    #add posts to the tok to be able to test 
    #keeps a previous views & comments to compare post viral video call
    prev_view:int = tok._tot_views
    prev_comment:int = tok._tot_comments
    tok.create_TikTok_post("GIOOOO")
    #0 representing index 0 in post list
    tok.viral_video(0)

    #since the comments and views is randomized, we check purely if it's greater!
    assert tok._tot_views > prev_view and tok._tot_comments > prev_comment



####REDDIT TESTING#####

def test_Reddit_init():
    t = Reddit("GIO", 1, 2, 3, 4)
    assert t._num_followers == 1
    assert t._num_posts == 2
    assert t._tot_upvote == 3
    assert t._tot_downvote == 4

def test_Reddit_display(capfd):
    test = Reddit("Eleven", 1,1,1,1)
    test.display()

    # Capture printed output
    out, err = capfd.readouterr()

    # Check expected strings
    assert "Username: Eleven" in out
    assert "Followers: 1" in out
    assert "Total upvotes: 1" in out
    assert "Total downvotes: 1" in out



def test_tot_karma():
    # Need to make sure tot_upvote && downvote are >= 0
    positive = Reddit("NAV", 1, 1, 50, 25)
    # 50-25
    assert positive.tot_karma() == 25


#
def test_tot_karma_negative_output():
    negative = Reddit("KDOT", 1, 1, 25, 50)
    # 25 -50 = -25; accounts can have negative total karma!!
    assert negative.tot_karma() == -25


#Makes sure upvote ratio raises error when no upvotes & downvotes
def test_tot_karma_no_karma():
    n = Reddit("JCOLE", 1, 1, 0, 0)
    with pytest.raises(ValueError):
        n.tot_karma() 
    

def test_average_upvotes():
    #raises if no posts 
    test = Reddit("GIOISCOOL", 1, 4, 1000, 25)
    assert test.average_upvotes() == 250


#Makes sure average upvotes raises error when 0 posts
def test_average_upvotes_no_posts():
    n = Reddit("LIL TECCA", 1, 0, 10, 10)
    with pytest.raises(ZeroDivisionError):
        n.average_upvotes() 


def test_upvote_ratio():
    test = Reddit("GIO", 1, 1, 50, 10)
    assert test.upvote_ratio() == .83


#Makes sure upvote ratio raises error when 0 posts
def test_upvote_ratio_no_posts():
    n = Reddit("CORDAE", 1, 0, 0, 0)
    with pytest.raises(ZeroDivisionError):
        n.upvote_ratio() 
    

