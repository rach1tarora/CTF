# Challenge Name
Key of Lost Secrets

## Cloud Service Provider Used
Microsoft Azure

## Story
In the mystical land of Eldoria, a powerful sorcerer sealed away a dark secret within a magical vault. The key to this vault is hidden in the tale of a prisoner who has rotted in a cell for 51 years. Only the bravest adventurers, armed with wisdom and courage, can decipher this tale to recover the lost vault and its sacred key. Uniting the key with the secret message will reveal the hidden truth, showing the way to save Eldoria from impending doom and granting you the final flag of victory.
(https://keylostsecrets.z5.web.core.windows.net/)

## Flag
FLAG-{B3C4r3fu1Ab0utD3l3t3dK3y5s3cr3t}

## Points & Difficulty
Score: Hard

## Hints
1. Use ROT51 to get username and password
2. Look for versioned secrets & keys.
3. Find a way to decrypt the encrypted text using the recovered key. ( use python )

## Services Used
Keyvault (Key,Secrets), Storageaccount (Static Website)

## Solution
Refer to the [solution/](./solution) directory for detailed scripts and explanations on how to decrypt the message and obtain the flag.

## Implementation Details
### Step-by-Step Implementation
1. **Key Vault Creation and Configuration**: 
   - Create an Azure Key Vault.
   - Configure the Key Vault access policy to grant necessary permissions to a dummy account.

2. **Key Management**: 
   - Create a key in the Key Vault.
   - Encrypt the first half of the flag using the key.
   - Delete the key after encryption.

3. **Secret Management**: 
   - Create a secret in the Key Vault with the second half of the flag.
   - Delete the secret after storing it.

4. **Static Website Creation**: 
   - Create a static website.
   - Encrypt the credentials using ROT13 and store them on the website.


## Additional Comments
This challenge integrates elements of Python scripting, cryptography, and Microsoft Azure.

## Contributor
- [@rach1tarora](https://twitter.com/rach1tarora)
