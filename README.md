# twish

<div align="center">
    <img src="twish.jpg" width="500px"/> 
</div>


Req.:
  - Read and Install xurl: https://github.com/xdevplatform/xurl
  - Rates Limits: https://docs.x.com/x-api/fundamentals/rate-limits
  - Auth: You must have a developer account and app to use xurl tool.


### Use o script como um comando
```bash
alias tw=<...path choice/tw>
```

### Autenticação
Na conta developer voce deverá obter os valores de BEATER TOKEN, CLIENT_ID e CLIENT_SECRET.
Esses valores serão utilizados primeiramente no script, em seguida autentique-se.
```bash
tw -auth
```

### Post um tweet
```bash
tw "New post!"
```

### Responda tweets
**Necessário obter id*
```bash
tw -rep <tweet_id> "reply"
```

### Delete tweets. 
**Necessário obter id*
```bash
tw -del <tweet_id>
```