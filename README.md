# Discord Bot in Python

## Client & Bot Classes

### 建立物件方式

* Client

```
client = discord.Client()
```

* Bot 

在使用```Bot```前，需先從子目錄```ext/commands```進行導入
```python 
from discord.ext import commands

bot = commands.Bot("!")
```
Bot物件中的參數```"!"```為在discord對bot使用指令所使用到的前綴，可以定義其他字元內容，完整寫法是
```python 
bot = commands.Bot(command_prefix="!")
```
### Missing required argument: 'intents'
在2.0版本後，這兩種類別都需要在新建物件時輸入intents參數，否則會出現
```Client.__init__() missing 1 required keyword-only argument: 'intents'``` 的error

```python
intents = discord.Intents.default()

client = discord.Client(intents=intents)
#or
bot = commands.Bot(command_prefix="!",intents=intents)
```

### 差異

```Bot``` 為```Client```的 subclass，```Bot``` 繼承了```Client``` 的所有功能，因此可以直接使用```Bot```來調用```Client```中所有屬性及方法，**需注意，不要同時使用這兩種Class。**

此外，```Bot```可以直接使用```@bot.command()```decorator來快速定義命令，而使用```Client```時必須手動處理事件


## 定義指令
使用```@bot.command()```定義指令，範例1：
```python
@bot.command()
async def hello(ctx):
    await ctx.send(f"!Hi <@{ctx.author.id}>")
```
* 定義的指令至少要有一個參數```ctx```，即當使用者輸入指令的Context。
* author是指輸入指令的使用者本人，透過ctx.author.id來取得該使用者的id，使對Bot輸入"!hello"即可讓Bot回傳一個"Hi"的訊息並標注輸入這則指令的使用者
* 執行後可能會出現discord.errors.PrivilegedIntentsRequired相關的error
，請參考下方的Privileged Intents Settings說明

### Privileged Intents Settings
由於指令定義的動作中會讀取使用者輸入的上下文作為參數，我們需要根據動作中所需要參照的內容來開通Discord Bot中的Privileged Intents。
* 首先登入[Discord Developers Applications page](https://discord.com/developers/applications)，並點選要開通Privileged Intents的Bot 
* 點選左方SETTINGS選單中的Bot選項

    ![](https://i.imgur.com/46WXqR0.png =40%x)
* 移動至“Privileged Gateway Intents”段落並根據需求開啟2對應的Intents
![](https://i.imgur.com/yTiPk1f.png)

* 三種類別的Intents說明如下
#### Presence Intent 
需要追蹤成員的狀態以及活動
#### Server Members Intent
需要取得成員的加入、離開、暱稱/身分組變更等事件
#### Message Content Intent
需要讀取成員發送訊息的上下文執行後續操作，指令也包括在其中，因為需要讓定義的指令判讀訊息是否含有特定的prefix

## Privileged message content intent is missing
出現此報錯是由於2.0整合更新後有所變動，需要將先前宣告的intents物件
```python 
intents = discord.Intents.default()
```
改成
```python 
intents = discord.Intents.all()
```

## Overriding the default ```on_message``` and ```@bot.command()``` Conflict  Issue

若是有覆寫預設的``` on_message ```function，將使得其他commands的運作失效，要解決此問題，需要在``` on_message ```的結尾添加 ```bot.process_commands(message)```

如：
```python
@bot.event
async def on_message(message):
    # do some extra stuff here

    await bot.process_commands(message)
```







### References


* https://discordpy.readthedocs.io/en/stable/migrating.html#intents-are-now-required
* https://stackoverflow.com/questions/51234778/what-are-the-differences-between-bot-and-client
* https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html
* https://discordpy.readthedocs.io/en/stable/intents.html
* https://discordpy.readthedocs.io/en/latest/faq.html#why-does-on-message-make-my-commands-stop-working
