# Solution to Key of Lost Secrets

Author: Rachit Arora 

Email: rachit27.arora@gmail.com

Link to resource:
- https://keylostsecrets.z5.web.core.windows.net/

## Overview

Azure: Azure supports versioning for both keys and secrets. In this challenge, the flag is divided into two parts. One part is encrypted with versioned keys, and the other part is stored in versioned secrets. Participants must write a Python script to decrypt the encrypted message using the versioned keys for one half of the flag and the versioned secrets for the other half.

## Challenge Details

- **Encrypted Message**: RSA 2048 encrypted string + Secret 

## Step-by-Step Solution

1. **View the Source Code**: Access the website and inspect the source code to find the credentials, which are encoded using ROT51.

    ```html
    <script>
       // Bqdcdmshzkr
       // Ftzqchzm'r Mzld: uztksftzqchzm@cqzfnmr-hm-sgd.bkntc
       // Sqdzrtqd Jdx: +a0Q-ol-5P$60pdS<T7C
       // Flag = '\x19\x03\xc4d"\\.\xab \xae\xa1\x08\xe6\xfb6A\xfe\x83n\\\xcf\xb2\xf2\xc8|\x97J\xcds^\xf0\xcfK\x95a\x7f\xe4U\x8d\xa8\x1b[k\x02W\x101\xd4\xaa\xc6\xf9\x11\xeb_\x04\x95kmP*\x1b}\x88\xfed\xf76\xbd\xde*XRP\xcb\xc1\t\xfa!\x83\x1d\xd7r\x95\xd7\x08\x80\xcfnn\xcf\xf6\xc1d\x8e\x0f\xfb7\xfa`=\xad\xc2\xbfMF6\xe1\x05\xf3\xa8\xd8Ky\xdckV3\xc5\xbev3\xbe\\\xc7U\x8c\x87V\x19#B\xfa\xd8#\x94\x9f\x84\x82~\xddg\xca\xe2\xfd\x80\xe4\xa3@\x12\x9be\x99e_\xf6\x91\x85sEef\'\xe9\x86\x99\xd1%\x85\x91{\xae\xb6M<n\x16\xa8\xe5\xe1\x1b\x07\x9e\x82\xcd\xa6r\xc7\xba\xcc\x9c\xe3\x0b\x93\xe5\x97\xc2\x04\x03\x88{,\xe5\x9fL\x0b\xe0^\x00\xc3\x8dn\x8f6N\xf0q\x92y\x8e\x08\x12>?{\x1a\xa6\xf5\xac\xd0t\\\x81\x10\xab\xaa\x8e8)\xd1GZ\xce\xe7\x95S9QN\xe2\xe1\xfb\xc9\xab\xbd\xbc\xad' + secret
    </script>
    </body>
    </html>
    ```

2. **Decode Credentials**: Use https://www.dcode.fr/rot-cipher to decode the credentials using ROT51.

    ```plaintext
    Credentials
    Guardian's Name: vaultguardian@dragons-in-the.cloud
    Treasure Key: +b0R-pm-5Q$60qeT<U7D
    ```

3. **Azure Login**:

Securely convert the password to a secure string:
```powershell
$securePassword = ConvertTo-SecureString '+b0R-pm-5Q$60qeT<U7D' -AsPlainText -Force
```

Create a PSCredential object with the username and secure password:
```powershell
$credential = New-Object System.Management.Automation.PSCredential("vaultguardian@dragons-in-the.cloud", $securePassword)
```

Connect to Azure using the provided credentials:
```powershell
Connect-AzAccount -Credential $credential
```

**Note:** There is a known bug in certain Azure PowerShell versions that affects the `Connect-AzAccount` command. When attempting to use `Get-AzKeyVaultKey` or any other Azure PowerShell command, you may encounter issues if you are using an older version of the Azure PowerShell module. This issue has been reported but not yet tested with newer versions. For more details, refer to [this GitHub issue](https://github.com/Azure/azure-powershell/issues/24967).

To resolve this problem, you can run the following command:
```powershell
Update-AzConfig -EnableLoginByWam $false
```

Alternatively, you can log in via the Azure CLI:

```markdown
az login
```
A web browser will open 

4. To enumerate Azure resources, use the following command:
```powershell
Get-AzResource
```

Example output:

**Resource:** SorcererStash
- **Resource Group:** KeyLostSecrets
- **Resource Type:** Microsoft.KeyVault/vaults
- **Location:** westus2
- **Resource ID:** /subscriptions/c10b781d-08d8-469e-856d-df629d08b294/resourceGroups/KeyLostSecrets/providers/Microsoft.KeyVault/vaults/SorcererStash
- **Tags:** None

**Resource:** MysticCoffer
- **Resource Group:** KeyLostSecrets
- **Resource Type:** Microsoft.KeyVault/vaults
- **Location:** westus2
- **Resource ID:** /subscriptions/c10b781d-08d8-469e-856d-df629d08b294/resourceGroups/KeyLostSecrets/providers/Microsoft.KeyVault/vaults/MysticCoffer
- **Tags:** None

**Resource:** keylostsecrets
- **Resource Group:** KeyLostSecrets
- **Resource Type:** Microsoft.Storage/storageAccounts
- **Location:** westus2
- **Resource ID:** /subscriptions/c10b781d-08d8-469e-856d-df629d08b294/resourceGroups/KeyLostSecrets/providers/Microsoft.Storage/storageAccounts/keylostsecrets
- **Tags:** None

**Resource:** InfernalLockbox
- **Resource Group:** KeyLostSecrets
- **Resource Type:** Microsoft.KeyVault/vaults
- **Location:** westus2
- **Resource ID:** /subscriptions/c10b781d-08d8-469e-856d-df629d08b294/resourceGroups/KeyLostSecrets/providers/Microsoft.KeyVault/vaults/InfernalLockbox
- **Tags:** None

5. To enumerate versioned keys in an Azure Key Vault, use the following command:
```powershell
Get-AzKeyVaultKey -VaultName "MysticCoffer" -Name "wyrmguard" -IncludeVersions
```

Example output:

**Key Vault:** mysticcoffer
- **Key Name:** wyrmguard
- **Version:** a2c446bf9a384c9586e9a1afa668a215
- **ID:** https://mysticcoffer.vault.azure.net:443/keys/wyrmguard/a2c446bf9a384c9586e9a1afa668a215
- **Enabled:** True
- **Created:** 12-07-2024 17:52:29
- **Updated:** 12-07-2024 17:52:29
- **Recovery Level:** Recoverable+Purgeable
- **Tags:** None

**Key Vault:** mysticcoffer
- **Key Name:** wyrmguard
- **Version:** 723254457f4248aaa1414b5d1c6e2ff3
- **ID:** https://mysticcoffer.vault.azure.net:443/keys/wyrmguard/723254457f4248aaa1414b5d1c6e2ff3
- **Enabled:** True
- **Created:** 12-07-2024 17:19:28
- **Updated:** 12-07-2024 17:19:28
- **Recovery Level:** Recoverable+Purgeable
- **Tags:** None

**Key Vault:** mysticcoffer
- **Key Name:** wyrmguard
- **Version:** 85261814726c4e1aaedccaf8f2eabca8
- **ID:** https://mysticcoffer.vault.azure.net:443/keys/wyrmguard/85261814726c4e1aaedccaf8f2eabca8
- **Enabled:** True
- **Created:** 28-06-2024 20:17:26
- **Updated:** 28-06-2024 20:17:26
- **Recovery Level:** Recoverable+Purgeable
- **Tags:** None

**Key Vault:** mysticcoffer
- **Key Name:** wyrmguard
- **Version:** dff1a19ccea84e2fbbd8c3187792a3a8
- **ID:** https://mysticcoffer.vault.azure.net:443/keys/wyrmguard/dff1a19ccea84e2fbbd8c3187792a3a8
- **Enabled:** True
- **Created:** 12-07

-2024 17:52:26
- **Updated:** 12-07-2024 17:52:26
- **Recovery Level:** Recoverable+Purgeable
- **Tags:** None

6. Decrypt the first half of the flag, use the recovered key and the provided file. Assuming you have the encrypted data and necessary information in a file, run the following command:

```shell
python decrypt_flag.py
```

This will output the decrypted first half of the flag:

```
Decrypted: FLAG-{B3C4r3fu1Ab0utD3
```

### Enumerating All Versioned Secrets

To list all versioned secrets in an Azure Key Vault, use the following command:

```powershell
Get-AzKeyVaultSecret -VaultName 'InfernalLockbox' -Name 'netherlock' -IncludeVersions
```

This command retrieves all versions of the secret named "netherlock" within the Key Vault "InfernalLockbox". It provides details such as the secret's ID, version, creation and update times, enabled status, and more.

Here are the details of the retrieved secrets:

**Vault Name:** infernallockbox
- **Secret Name:** netherlock
  - **Version:** 24f684944e984e2997278477c7702c49
  - **ID:** https://infernallockbox.vault.azure.net:443/secrets/netherlock/24f684944e984e2997278477c7702c49
  - **Enabled:** True
  - **Created:** 12-07-2024 17:46:44
  - **Updated:** 12-07-2024 17:46:44
  - **Content Type:** 
  - **Tags:** None

**Vault Name:** infernallockbox
- **Secret Name:** netherlock
  - **Version:** 681e0661321648a5a0d74ed2a55353b6
  - **ID:** https://infernallockbox.vault.azure.net:443/secrets/netherlock/681e0661321648a5a0d74ed2a55353b6
  - **Enabled:** True
  - **Created:** 12-07-2024 17:46:38
  - **Updated:** 12-07-2024 17:46:38
  - **Content Type:** 
  - **Tags:** None

**Vault Name:** infernallockbox
- **Secret Name:** netherlock
  - **Version:** b5ce1490ab2a4e419f7224b2c6220aae
  - **ID:** https://infernallockbox.vault.azure.net:443/secrets/netherlock/b5ce1490ab2a4e419f7224b2c6220aae
  - **Enabled:** True
  - **Created:** 12-07-2024 17:40:32
  - **Updated:** 12-07-2024 17:40:32
  - **Content Type:** 
  - **Tags:** None

**Vault Name:** infernallockbox
- **Secret Name:** netherlock
  - **Version:** c859cdbbd0bb4b1c9a0af59a2a673f38
  - **ID:** https://infernallockbox.vault.azure.net:443/secrets/netherlock/c859cdbbd0bb4b1c9a0af59a2a673f38
  - **Enabled:** True
  - **Created:** 12-07-2024 17:40:42
  - **Updated:** 12-07-2024 17:40:42
  - **Content Type:** 
  - **Tags:** None

**Vault Name:** infernallockbox
- **Secret Name:** netherlock
  - **Version:** c959ae7b26a44ef8a9a121f8f2ad1653
  - **ID:** https://infernallockbox.vault.azure.net:443/secrets/netherlock/c959ae7b26a44ef8a9a121f8f2ad1653
  - **Enabled:** True
  - **Created:** 12-07-2024 17:40:56
  - **Updated:** 12-07-2024 17:40:56
  - **Content Type:** 
  - **Tags:** None

**Vault Name:** infernallockbox
- **Secret Name:** netherlock
  - **Version:** f85115427edb43aca4f3f7760210f39a
  - **ID:** https://infernallockbox.vault.azure.net:443/secrets/netherlock/f85115427edb43aca4f3f7760210f39a
  - **Enabled:** True
  - **Created:** 28-06-2024 20:30:42
  - **Updated:** 28-06-2024 20:30:42
  - **Content Type:** 
  - **Tags:** None

### Reading the Secret

Retrieve the specific version of the secret that contains the other half of the flag:
```powershell
Get-AzKeyVaultSecret -VaultName 'infernallockbox' -Name 'netherlock' -Version 'f85115427edb43aca4f3f7760210f39a' -AsPlainText
```

The output will be:
```
l3t3dK3y5s3cr3t}
```

**Combine and Retrieve the Full Flag**: Combine the decrypted first half and the recovered second half of the flag to get the complete flag.

```
FLAG-{B3C4r3fu1Ab0utD3l3t3dK3y5s3cr3t}
```