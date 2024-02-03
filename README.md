# cloud

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/cloud)
[![General Workflow](https://github.com/rolehippie/cloud/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/cloud/actions/workflows/general.yml)
[![Readme Workflow](https://github.com/rolehippie/cloud/actions/workflows/docs.yml/badge.svg)](https://github.com/rolehippie/cloud/actions/workflows/docs.yml)
[![Galaxy Workflow](https://github.com/rolehippie/cloud/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/cloud/actions/workflows/galaxy.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/cloud)](https://github.com/rolehippie/cloud/blob/master/LICENSE)
[![Ansible Role](https://img.shields.io/badge/role-rolehippie.cloud-blue)](https://galaxy.ansible.com/rolehippie/cloud)

Ansible role to install cli for multiple cloud providers.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [cloud_awscli_arch](#cloud_awscli_arch)
  - [cloud_awscli_enabled](#cloud_awscli_enabled)
  - [cloud_awscli_installer](#cloud_awscli_installer)
  - [cloud_azure_arch](#cloud_azure_arch)
  - [cloud_azure_enabled](#cloud_azure_enabled)
  - [cloud_azure_keyring](#cloud_azure_keyring)
  - [cloud_eksctl_arch](#cloud_eksctl_arch)
  - [cloud_eksctl_download](#cloud_eksctl_download)
  - [cloud_eksctl_enabled](#cloud_eksctl_enabled)
  - [cloud_eksctl_version](#cloud_eksctl_version)
  - [cloud_hcloud_arch](#cloud_hcloud_arch)
  - [cloud_hcloud_download](#cloud_hcloud_download)
  - [cloud_hcloud_enabled](#cloud_hcloud_enabled)
  - [cloud_hcloud_version](#cloud_hcloud_version)
  - [cloud_install_path](#cloud_install_path)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.10`

## Default Variables

### cloud_awscli_arch

#### Default value

```YAML
cloud_awscli_arch: "{{ 'aarch64' if ansible_architecture == 'aarch64' else 'x86_64'
  }}"
```

### cloud_awscli_enabled

Enable installation of aws cli

#### Default value

```YAML
cloud_awscli_enabled: true
```

### cloud_awscli_installer

URL to download installer from

#### Default value

```YAML
cloud_awscli_installer: https://awscli.amazonaws.com/awscli-exe-linux-{{ cloud_awscli_arch
  }}.zip
```

### cloud_azure_arch

Architecture for azure

#### Default value

```YAML
cloud_azure_arch: "{{ 'arm64' if ansible_architecture == 'aarch64' else 'amd64' }}"
```

### cloud_azure_enabled

Enable installation of azure cli

#### Default value

```YAML
cloud_azure_enabled: true
```

### cloud_azure_keyring

Path for the repository keyring

#### Default value

```YAML
cloud_azure_keyring: /usr/share/keyrings/microsoft-archive-keyring.gpg
```

### cloud_eksctl_arch

Architecture for eksctl

#### Default value

```YAML
cloud_eksctl_arch: "{{ 'arm64' if ansible_architecture == 'aarch64' else 'amd64' }}"
```

### cloud_eksctl_download

URL to download eksctl from

#### Default value

```YAML
cloud_eksctl_download: https://github.com/weaveworks/eksctl/releases/download/v{{
  cloud_eksctl_version }}/eksctl_Linux_{{ cloud_eksctl_arch }}.tar.gz
```

### cloud_eksctl_enabled

Enable installation of eksctl cli

#### Default value

```YAML
cloud_eksctl_enabled: true
```

### cloud_eksctl_version

Version of eksctl to install

#### Default value

```YAML
cloud_eksctl_version: 0.170.0
```

### cloud_hcloud_arch

Architecture for hcloud

#### Default value

```YAML
cloud_hcloud_arch: "{{ 'arm64' if ansible_architecture == 'aarch64' else 'amd64' }}"
```

### cloud_hcloud_download

URL to download hcloud from

#### Default value

```YAML
cloud_hcloud_download: https://github.com/hetznercloud/cli/releases/download/v{{ cloud_hcloud_version
  }}/hcloud-linux-{{ cloud_hcloud_arch }}.tar.gz
```

### cloud_hcloud_enabled

Enable installation of hcloud cli

#### Default value

```YAML
cloud_hcloud_enabled: true
```

### cloud_hcloud_version

Version of hcloud to install

#### Default value

```YAML
cloud_hcloud_version: 1.42.0
```

### cloud_install_path

Path to install the binaries

#### Default value

```YAML
cloud_install_path: /usr/bin
```

## Discovered Tags

**_awscli_**

**_azure_**

**_cloud_**

**_eksctl_**

**_hcloud_**


## Dependencies

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
