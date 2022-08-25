# CSE 212 | Programming with Data Structures

## GitHub Pages Setup
### Actions
When changes are pushed to the **Main** branch, a GitHub [action](https://github.com/byui-cse/cse212-csharp/actions) is started to deploy the content. It takes roughly 1 minute to deploy, but that could change as the size of the project changes

## Run Local Setup
### Prerequisites
* [Jekyll for Ruby](https://jekyllrb.com/docs/installation/)

### Setup
Using terminal window in the `/docs` folder, run

```bash
bundle install
```

### Run
Using terminal window in the `/docs` folder, run

```bash
bundle exec jekyll serve --config local-config.yml
```

### Temporary files
The following folders / files will be added to your `/docs` folder that should not be committed to GitHub:
* `_site/`
* `.jekyll-cache/`
* `Gemfile.lock`
