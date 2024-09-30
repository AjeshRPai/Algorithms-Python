from typing import List
from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.tweet_count = 0  # Global counter for tweets
        self.user_tweets = defaultdict(list)  # Store tweets for each user
        self.following = defaultdict(set)  # Track who each user is following

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Add new tweet to user's tweet list with a timestamp
        self.user_tweets[userId].append((self.tweet_count, tweetId))
        self.tweet_count -= 1  # Decrement to keep most recent tweets at the top

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        max_heap = []  # Use max heap to get most recent tweets

        # Include user's own tweets
        self.following[userId].add(userId)

        # Collect most recent tweet from each followed user
        for followee_id in self.following[userId]:
            if followee_id in self.user_tweets and self.user_tweets[followee_id]:
                tweet = self.user_tweets[followee_id][-1]
                heapq.heappush(max_heap, (-tweet[0], tweet[1], followee_id, len(self.user_tweets[followee_id]) - 1))

        # Collect top 10 most recent tweets
        while max_heap and len(tweets) < 10:
            _, tweet_id, followee_id, idx = heapq.heappop(max_heap)
            tweets.append(tweet_id)

            # If there are more tweets from this user, add the next one to the heap
            if idx > 0:
                next_tweet = self.user_tweets[followee_id][idx-1]
                heapq.heappush(max_heap, (-next_tweet[0], next_tweet[1], followee_id, idx-1))

        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)  # Use discard to avoid KeyError