SELECT * FROM getoldtweets3_tweet.final_blacklivesmatter_minnesota 
WHERE tweet_created_dt > '2020-05-25 23:59:59' AND tweet_created_dt < '2020-06-02 00:00:00'
order by retweets desc