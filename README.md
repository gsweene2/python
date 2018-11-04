# Adding an entity to an AWS Trust Document

## The Problem

There is not a way to add a trusted entity to an IAM Role's Trust Document via the AWS CLI.

The current process is to
1. Get the current Policy Document via AWS CLI
2. Manually add the ARN
3. Update the Policy Document via AWS CLI

## The Solution

A python script that takes (1) the cross account role and (2) the trusted entity as parameters, and performs the operation in a one line command.

# Example

## Command
```
$ python3 add_entity_to_trust_document.py cross-account-role arn:aws:iam::753904353427:root
```

## Output
```
The AWS key is a list of arn
Value appended
The resulting trust document:
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::753904353427:root",
          "arn:aws:iam::085183144779:root",
          "arn:aws:iam::753904353427:root"
        ]
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "Bool": {
          "aws:MultiFactorAuthPresent": "true"
        }
      }
    }
  ]
}
```