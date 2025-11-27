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


#def __init__(self, username: str, num_followers: int, posts: int likes: int, reposts: int):
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
    t2 = Instagram("Gio", 10, 3, 300, 0)

    #Makes sure either an int or float
    assert isinstance(s.repost_rate(), (int, float))

    #divides (reposts / followers) * 100 
    assert s.repost_rate() == 2

    #when reposts is 0 and followers >= 1
    assert t2.repost_rate() == 0



#Covers when no posts are made  (Divide by 0)
def test_respost_rate_zero_followers():
    with pytest.raises(ZeroDivisionError):
        noFollowers = Instagram("Gio", 0, 0, 0, 10)
        noFollowers.repost_rate()




#TIKTOK TESTS
def test_comment_view_conversion_rate():
    t = TikTok("Ramiro", 22, 1, 30, 60)
    
    assert isinstance(t.comment_view_conversion_rate(), (int, float))
    #testing 30/60 == .5 * 100
    assert t.comment_view_conversion_rate() == 50


def test_avg_comment_per_post():
    tik = TikTok("Vere", 1, 20, 100, 1)

    assert isinstance(tik.avg_comment_per_post(), (int, float))
    #testing 100/20 == 5
    assert tik.avg_comment_per_post() == 5



def test_viral_video():
    tok = TikTok("Lucas", 1, 1, 1, 1)
    #add posts to the tok to be able to test 
    #keeps a previous views & comments to compare post viral video call
    prev_view:int = tok._tot_views
    prev_comment:int = tok._tot_comments
    tok.viral_video()

    #since the comments and views is randomized, we check purely if it's greater!
    assert tok._tot_views > prev_view and tok._tot_comments > prev_comment



def test_tot_karma():
    # Need to make sure tot_upvote && downvote are >= 0
    positive = Reddit("GIOISCOOL", 1, 1, 50, 25)
    negative = Reddit("GIOISCOOL2", 1, 1, 25, 50)
    # 50-25
    assert positive.tot_karma() == 25
    # 25 -50 = -25; accounts can have negative total karma!!
    assert negative.tot_karma() == -25
    

def test_average_upvotes():
    #raises if no posts 
    test = Reddit("GIOISCOOL", 1, 4, 1000, 25)
    assert test.average_upvotes() == 250


def test_upvote_ratio():
    test = Reddit("GIO", 1, 1, 50, 10)
    assert test.upvote_ratio() == .83


