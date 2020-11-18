import torch
from torch.utils.data import Dataset


class TweetTextDataset(Dataset):
    def __init__(self, tweet_texts, targets, tokenizer, max_len):
        self.tweet_texts = tweet_texts
        self.targets = targets
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.tweet_texts)

    def __getitem__(self, item):
        tweet_text = str(self.tweet_texts[item])
        target = self.targets[item]

        encoding = self.tokenizer.encode_plus(
            tweet_text,
            add_special_tokens=True,
            max_length=self.max_len,
            truncation=True,
            padding='max_length',
            return_token_type_ids=False,
            pad_to_max_length=True,
            return_attention_mask=True,
            return_tensors='pt'
        )

        return {
            'tweet_text': tweet_text,
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'targets': torch.tensor(target, dtype=torch.long)
        }
