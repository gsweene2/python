import json

aws_json = '''
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::085183144779:root"
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
'''

data = json.loads(aws_json)

new_arn = "arn:aws:iam::753904353427:root"

value = data["Statement"][0]["Principal"]["AWS"]
kind = isinstance(value, str)

if (kind): 
    print("The AWS key is a string arn")
    newValue = []
    newValue.append(value)
    newValue.append(new_arn)
    data["Statement"][0]["Principal"]["AWS"] = newValue
    print("Value appended")
else:
    print("The AWS key is a list of arn")
    value.append(new_arn)
    print("Value appended")

# Back to string
new_string = json.dumps(data, indent=2)    
print()
print()
print()
print(new_string)

