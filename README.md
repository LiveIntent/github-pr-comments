# Github PR collapsible comments

Post comments on PRs and issues and delete the old ones that were created before. It will delete only the messages that it wrote before.
For example, this tool is useful to post tfsec report for a terraform repository.

## Inputs

## `pr_number`
**Required** The PR number where to post the message to.

## `filename`
**Required** The filename path that will be read and post is content as comment.

## `title`
**Optional** A short description for the collapsible comment.

## Example usage

```yaml
- uses: liveintent/github-pr-comments@main
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  with:
    pr_number: ${{ github.event.number }}
    filename: "tfsec-output.txt"
    title: "tfsec report"
```

### Github action example

```yaml
name: Terraform

on: pull_request

jobs:
  tfsec:
    name: TFSEC
    runs-on: ubuntu-22.04

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: tfsec
        id: tfsec_step
        uses: aquasecurity/tfsec-action@v1.0.0
        with:
          additional_args: "--no-color --out tfsec-output.txt"
          soft_fail: true

      - uses: liveintent/github-pr-comments@v0.1.0
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          pr_number: ${{ github.event.number }}
          filename: "tfsec-output.txt"
          title: "TFsec report"
```
