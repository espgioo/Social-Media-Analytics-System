import pytest
from bst import Node, BST
from social import Instagram, TikTok, Reddit

def test_node_init_and_getters():
    gio = Instagram("Gio", 1, 1, 1, 1)
    node = Node(gio, 1)
    assert node.get_left() is None
    assert node.get_right() is None
    assert node.get_social_data() is gio
    assert node.get_social_type() == 1

def test_node_set_get_left():
    parent = Node(Instagram("Gio", 1, 1, 1, 1), 1)
    child = Node(Instagram("Brandon", 1, 1, 1, 1), 1)
    parent.set_left(child)
    assert parent.get_left() is child
    assert parent.get_right() is None

def test_node_set_get_right():
    parent = Node(Instagram("Gio", 1, 1, 1, 1), 1)
    child = Node(Instagram("Miguel", 1, 1, 1, 1), 1)
    parent.set_right(child)
    assert parent.get_right() is child
    assert parent.get_left() is None

def test_node_left_and_right_independent():
    parent = Node(Instagram("Gio", 1, 1, 1, 1), 1)
    left = Node(Instagram("Alex", 1, 1, 1, 1), 1)
    right = Node(Instagram("Mia", 1, 1, 1, 1), 1)
    parent.set_left(left)
    parent.set_right(right)
    assert parent.get_left() is left
    assert parent.get_right() is right

def test_BST_init():
    tree = BST()
    assert tree._root is None

def test_insert_Node():
    tree = BST()
    gio = Instagram("Gio", 1, 1, 1, 1)
    node = tree.insert_node(gio, 1)
    assert tree._root == node
    assert node.get_social_data().get_name() == "Gio"

def test_insert_left_child():
    tree = BST()
    root = tree.insert_node(Instagram("Gio", 1, 1, 1, 1), 1)
    tree.insert_node(Instagram("Alex", 1, 1, 1, 1), 1)
    assert root.get_left().get_social_data().get_name() == "Alex"

def test_insert_right_child():
    tree = BST()
    root = tree.insert_node(Instagram("Gio", 1, 1, 1, 1), 1)
    tree.insert_node(Instagram("Mia", 1, 1, 1, 1), 1)
    assert root.get_right().get_social_data().get_name() == "Mia"

def test_display_empty_tree_raises():
    tree = BST()
    with pytest.raises(ValueError):
        tree.display()

def test_display_prints_usernames(capsys):
    tree = BST()
    tree.insert_node(Instagram("Gio", 1, 1, 1, 1), 1)
    tree.insert_node(Instagram("Alex", 1, 1, 1, 1), 1)
    tree.insert_node(Instagram("Mia", 1, 1, 1, 1), 1)
    tree.display()
    out = capsys.readouterr().out
    assert "Username: Alex" in out
    assert "Username: Gio" in out
    assert "Username: Mia" in out

def test_retrieve_Node():
    tree = BST()
    tree.insert_node(Instagram("Gio", 1, 1, 1, 1), 1)
    tree.insert_node(Instagram("ISTHATYOUCASTRO", 1, 1, 1, 1), 1)
    tree.insert_node(TikTok("NOTFORRADIO", 1, 1, 1, 1), 2)
    tree.insert_node(Reddit("Ssirski", 1, 1, 1, 1), 3)
    assert tree.retrieve("Ssirski") is not None

def test_retrieve_empty_tree_raises():
    tree = BST()
    with pytest.raises(ValueError):
        tree.retrieve("Gio")

def test_retrieve_Node_account_non_existant():
    tree = BST()
    tree.insert_node(Instagram("Gio", 1, 1, 1, 1), 1)
    with pytest.raises(ValueError):
        tree.retrieve("ACCDOESNOTEXIST")

def test_find_dupe_dupe_found():
    tree = BST()
    tree.insert_node(Instagram("Gio", 1, 1, 1, 1), 1)
    with pytest.raises(ValueError):
        tree.find_dupe("Gio")

def test_find_dupe_no_dupe_on_tree():
    tree = BST()
    tree.insert_node(Instagram("Gio", 1, 1, 1, 1), 1)
    assert tree.find_dupe("Lucas") is True

def test_find_dupe_empty_tree_returns_true():
    tree = BST()
    assert tree.find_dupe("Gio") is True

def test_remove_account_from_empty_tree():
    tree = BST()
    with pytest.raises(ValueError):
        tree.remove_account("Gio")

def test_remove_account_only_root():
    tree = BST()
    tree.insert_node(Instagram("Gio", 1, 1, 1, 1), 1)
    tree.remove_account("Gio")
    assert tree._root is None

def test_remove_account_leaf_non_root():
    tree = BST()
    tree.insert_node(Instagram("Gio", 1, 1, 1, 1), 1)
    tree.insert_node(Instagram("Alex", 1, 1, 1, 1), 1)
    new_root = tree.remove_account("Alex")
    assert new_root is tree._root
    assert tree._root.get_social_data().get_name() == "Gio"
    assert tree._root.get_left() is None

def test_remove_account_root_with_only_left_child():
    tree = BST()
    tree.insert_node(Instagram("Max", 1, 1, 1, 1), 1)
    tree.insert_node(Instagram("Gio", 1, 1, 1, 1), 1)
    new_root = tree.remove_account("Max")
    assert new_root is tree._root
    assert tree._root.get_social_data().get_name() == "Gio"

def test_remove_account_root_with_only_right_child():
    tree = BST()
    tree.insert_node(Instagram("Gio", 1, 1, 1, 1), 1)
    tree.insert_node(Instagram("Mia", 1, 1, 1, 1), 1)
    new_root = tree.remove_account("Gio")
    assert new_root is tree._root
    assert tree._root.get_social_data().get_name() == "Mia"

def test_remove_account_root_with_two_children_uses_IOS():
    tree = BST()
    tree.insert_node(Instagram("Gio", 1, 1, 1, 1), 1)
    tree.insert_node(Instagram("Alex", 1, 1, 1, 1), 1)
    tree.insert_node(Instagram("Mia", 1, 1, 1, 1), 1)
    tree.insert_node(Instagram("Leo", 1, 1, 1, 1), 1)
    new_root = tree.remove_account("Gio")
    assert new_root is tree._root
    assert tree._root.get_social_data().get_name() == "Leo"
    assert tree._root.get_left().get_social_data().get_name() == "Alex"
    assert tree._root.get_right().get_social_data().get_name() == "Mia"

def test_remove_account_non_existent_name_raises():
    tree = BST()
    tree.insert_node(Instagram("Gio", 1, 1, 1, 1), 1)
    with pytest.raises(ValueError):
        tree.remove_account("Lucas")

def test_find_IOS_returns_leftmost_node():
    tree = BST()
    tree.insert_node(Instagram("Gio", 1, 1, 1, 1), 1)
    tree.insert_node(Instagram("Mia", 1, 1, 1, 1), 1)
    tree.insert_node(Instagram("Leo", 1, 1, 1, 1), 1)
    ios_node = tree.find_IOS(tree._root.get_right())
    assert ios_node.get_social_data().get_name() == "Leo"

def test_direct_to_social_menus_instagram_called(monkeypatch):
    tree = BST(); acc = Instagram("Gio", 1, 1, 1, 1); tree.insert_node(acc, 1)
    called = {"menu": None, "user": None}
    def fake_menu(user): called.update(menu="instagram", user=user)
    monkeypatch.setattr(tree, "Instagram_menu", fake_menu)
    result = tree.direct_to_social_menus("Gio")
    assert result is tree._root
    assert called["menu"] == "instagram"
    assert called["user"] is acc

def test_direct_to_social_menus_tiktok_called(monkeypatch):
    tree = BST(); acc = TikTok("GioTok", 1, 1, 1, 1); tree.insert_node(acc, 2)
    called = {"menu": None, "user": None}
    def fake_menu(user): called.update(menu="tiktok", user=user)
    monkeypatch.setattr(tree, "TikTok_menu", fake_menu)
    tree.direct_to_social_menus("GioTok")
    assert called["menu"] == "tiktok"
    assert called["user"] is acc

def test_direct_to_social_menus_reddit_called(monkeypatch):
    tree = BST(); acc = Reddit("GioReddit", 1, 1, 1, 1); tree.insert_node(acc, 3)
    called = {"menu": None, "user": None}
    def fake_menu(user): called.update(menu="reddit", user=user)
    monkeypatch.setattr(tree, "Reddit_menu", fake_menu)
    tree.direct_to_social_menus("GioReddit")
    assert called["menu"] == "reddit"
    assert called["user"] is acc

def test_direct_to_social_menus_raises_when_user_not_found():
    tree = BST()
    with pytest.raises(ValueError):
        tree.direct_to_social_menus("Nope")

def test_instagram_menu_exit_immediately(monkeypatch):
    tree = BST(); user = Instagram("Gio", 1, 1, 1, 1)
    monkeypatch.setattr("builtins.input", lambda _: "7")
    assert tree.Instagram_menu(user) is user

def test_tiktok_menu_exit_immediately(monkeypatch):
    tree = BST(); user = TikTok("GioTok", 1, 1, 1, 1)
    monkeypatch.setattr("builtins.input", lambda _: "7")
    assert tree.TikTok_menu(user) is user

def test_reddit_menu_exit_immediately(monkeypatch):
    tree = BST(); user = Reddit("GioReddit", 1, 1, 1, 1)
    monkeypatch.setattr("builtins.input", lambda _: "7")
    assert tree.Reddit_menu(user) is user

