# Aristocrat Banano auto gambler

*This project was an absolute joke and I'm genuinely surprised about how easy it was*

*This is more of a blog post rather than a project, but I do not presently have a blog. Maybe I should make this my first contribution to Medium?*

## The Idea
The Aristocrat method/ Monte-Carlo method/ Martingale method is a very simple approach to playing roulette or any other game where you make a stake and have ~50% chance of winning. The conditions are you need to have near infinite money and make low stakes. Every time you win, you take the winnings and place the initial amount back on, and every time you lose you double your stake, so eventually you will win. More info [here](https://en.wikipedia.org/wiki/Martingale_(betting_system)).

By coding a small selenium python script I was able to reliably (eventually) win back my original stake.

## Banano?
I have recently become fascinated by all things Blockchain and Crypto (I might also look into writing a real crypto trading bot, stay tuned for that). And in the vast oceans of altcoins I discovered [NANO](https://nano.org)! Nano is a feeless, near instant, green cryptocurrency with a ±human friendly codebase. Like Bitcin's Dogecoin, Nano has a meme fork: Banano (Currently worth around $0.004878). Now banano is fun, but not super useful at the moment. You can earn banano through community drops (which I haven't had much luck with yet), and, more interestingly, through Folding.

## F@H?
Folding@Home is an amazing project that allows everyone to use their spare computational power to simulate protein folding and help the world fight disease, and The Banano Project in incentivizing users by rewarding them with bananos. (Which is currenly my main source of bananos).

## Gambling?
Banano has an awesome gambling site [here](bananobet.com). It's a harmless fun, dopamine releasing source of disappointment (when you eventually lose). But is very simple and doesn't seem to have very advanced bot detection!

## The process
Very simple. Make a bet, if you lose then double the amount and make it again. I used selenium to dynamically set bet amounts, click the bet button and check the user balance. For more info on the process, visit my self documenting script!
