These directory contains the agents you can choose from to let Chat GPT assume different roles.

# Choose a different agent

When starting BloggerAgent you will be asked to
choose which agent to use for you next blog post.

All the .yaml/.yml files in this directory will
be automatically included at that point.

# Create a new agent

To create a new agent you should use the following
yaml keys.

### name

Name that will be used for the bot

### role

The role assumed by the bot
```
you're a crypto expert
```


### emotional_tone

The tone used by the bot

example:
```
youthful writing, accessible and trustable
```

### competency

The set of skills the bot has

example:
```
- Seo expert
```

### workflow

The process followed when writing a blog post

example:
```
- write an outline
- search on the internet for sources
```

### goal

The bot final goal, the title or any extra information
about the blog post its going to write