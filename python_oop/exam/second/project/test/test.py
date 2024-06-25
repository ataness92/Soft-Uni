from unittest import TestCase, main

from project.social_media import SocialMedia


class TestSocialMedia(TestCase):

    def setUp(self) -> None:
        self.social_media = SocialMedia('atanas', 'Instagram', 10, 'football')
        #self.social_media_incorrect = SocialMedia('plami', 'FaceBook', 1, 'english')

    def test_correct_init(self):
        self.assertEqual('atanas', self.social_media._username)
        self.assertEqual('Instagram', self.social_media.platform)
        self.assertEqual(10, self.social_media._followers)
        self.assertEqual('football', self.social_media._content_type)
        self.assertEqual([], self.social_media._posts)


    def test_incorrect_init_for_incorrect_platform(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media_incorrect = SocialMedia('plami', 'FaceBook', 1, 'english')

        self.assertEqual("Platform should be one of ['Instagram', 'YouTube', 'Twitter']", str(ve.exception))

    def test_incorrect_init_for_negative_number_of_followers(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.followers = -10

        self.assertEqual("Followers cannot be negative.", str(ve.exception))

    def test_incorrect_set_for_incorrect_platform(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.platform = 'Facebook'

        self.assertEqual("Platform should be one of ['Instagram', 'YouTube', 'Twitter']", str(ve.exception))

    def test_creating_of_a_post(self):
        result = self.social_media.create_post("new_match_results")
        expected_post_result = {'content': 'new_match_results', 'likes': 0, 'comments': []}
        self.assertEqual(f"New football post created by atanas on Instagram.", result)
        self.assertEqual(expected_post_result, self.social_media._posts[-1])
        self.assertEqual([expected_post_result], self.social_media._posts)

    def test_correct_like_of_post_check_liked_by_username(self):
        self.social_media.create_post("new_match_results")
        result = self.social_media.like_post(0)
        expected_like_result = {'content': 'new_match_results', 'likes': 1, 'comments': []}
        self.assertEqual(expected_like_result, self.social_media._posts[-1])
        self.assertEqual([expected_like_result], self.social_media._posts)
        self.assertEqual(f"Post liked by atanas.", result)

    def test_incorrect_like_of_post_too_many_times(self):
        self.social_media.create_post("new_match_results")
        for i in range(15):
            result = self.social_media.like_post(0)
        self.assertEqual(f"Post has reached the maximum number of likes.", result)

    def test_incorrect_like_of_post_invalid_post_index(self):
        self.social_media.create_post("new_match_results")
        result = self.social_media.like_post(1)
        self.assertEqual(f"Invalid post index.", result)

    def test_comment_on_post_with_less_chars(self):
        result = self.social_media.create_post("new_match_results")
        result = self.social_media.comment_on_post(0, "like")

        self.assertEqual("Comment should be more than 10 characters.", result)

    def test_comment_on_post_with_coorect_num_of_chars(self):
        result = self.social_media.create_post("new_match_results")
        result = self.social_media.comment_on_post(0, "Hi Plamena, I really liked your post!")

        self.assertEqual("Comment added by atanas on the post.", result)
        comment_result = self.social_media._posts[0]['comments']
        self.assertEqual([{'user': 'atanas', 'comment': "Hi Plamena, I really liked your post!"}], comment_result)
