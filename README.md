# twish

<div align="center">
    <img src="twish.jpg" width="500px"/> 
</div>

## Requirements:
  - Read and Install xurl: [https://github.com/xdevplatform/xurl](https://github.com/xdevplatform/xurl)
  - Rate Limits: [https://docs.x.com/x-api/fundamentals/rate-limits](https://docs.x.com/x-api/fundamentals/rate-limits)
  - Authentication: You must have a developer account and an app to use the xurl tool.

### Use the script as a command
```bash
alias tw=<...path choice/tw>
```

### Authentication
In the developer account, you need to obtain the values for BEARER TOKEN, CLIENT_ID, and CLIENT_SECRET.  
These values will first be used in the script, then authenticate yourself.  
```bash
tw -auth
```

### Post a tweet
```bash
tw "New post!"
```

...With media
```bash
tw "New post!" image.jpg
```

```bash
tw "New post!" https://anyurl-image.up/image.jpg
```

### Reply to tweets
**You need to obtain the ID**
```bash
tw -rep <tweet_id> "reply"
```

### Delete tweets  
**You need to obtain the ID**
```bash
tw -del <tweet_id>
```