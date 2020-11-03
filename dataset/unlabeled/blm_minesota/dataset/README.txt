SELECT text
FROM getoldtweets3_tweet.final_blacklivesmatter_minnesota 
WHERE tweet_created_dt > '2020-05-24 23:59:59' AND tweet_created_dt < '2020-06-01 00:00:00'
AND (retweets > 100 or favorites > 100)
order by retweets desc