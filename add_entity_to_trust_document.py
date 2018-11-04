import json
import os
import sys

cross_account_role = sys.argv[1]
new_arn = sys.argv[2]

# cross_account_role = "cross-account-role"
# new_arn = "arn:aws:iam::753904353427:root"

aws_json = os.popen("aws iam get-role --role-name " + cross_account_role).read()

# Convert to object
data = json.loads(aws_json)

value = data["Role"]["AssumeRolePolicyDocument"]["Statement"][0]["Principal"]["AWS"]
kind = isinstance(value, str)

# is a string or list of entities
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

new_policy_document = data["Role"]["AssumeRolePolicyDocument"]

# Back to string
new_role = json.dumps(data, indent=2)
new_policy_document_string = json.dumps(new_policy_document, indent=2)

# Print new policy to file
with open('new_policy_document.json', 'a') as policy_document_file:
    policy_document_file.write(new_policy_document_string)

# Update Role in AWS
os.popen("aws iam   update-assume-role-policy --role-name " + cross_account_role + " --policy-document file://new_policy_document.json").read()

# Clean up the file
os.remove("new_policy_document.json")

# Print results
print("The resulting trust document:")
print(new_policy_document_string)
