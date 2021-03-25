# geekoops-next

Install and configure a NEXT (Network Boot) server using `dnsmasq`.

Note: EFI boot is not yet working (missing files in ``next.tar.gz`).

## Role Variables


| Value | Description | Default |
|-------|-------------|---------|
|`dns_port`| DNS port to use | 0 (disabled) |
|`dhcp_no_override` | Set `dhcp_no_override` for compatability with old clients | true |
|`dhcp_boot` | Set PXE boot file | `pxelinux.0` |
|`prompt` | Set boot prompt test | "geekoops-next Network boot" |
|`prompt_timeout` | Set boot prompt timeout in seconds | 2 |
|`legacy` | Use legacy boot | true |
|`efi` | Use EFI boot (not yet working) | true |
|`dhcp_range` | `dhcp_range` directive for `dnsmasq` | "" (disabled) |
|`config_firewall` | Configure firewall | false |
|`firewall_zone` | Firewall zone to configure | "public" |

## Example Playbook

    - hosts: jellyfish
      roles:
         - { role: geekoops-next }

More extended example, where we use "192.168.122.1" as DHCP server (i.e. the NEXT server is only DHCP proxy). This works well in case you want to use an external DHCP server and use another machine as NEXT server without providing DHCP.

    - hosts: jellyfish
      roles:
         - role: geekoops-next
           vars:
             config_firewall: true
             firewall_zone: "public"
             dhcp_range: "192.168.122.1,proxy,255.255.255.0"
             prompt: "My awesome network boot server"

## License

MIT

## Author Information

phoenix

Have a lot of fun!

# Development

## syslinux

Get the latest `syslinux` from [kernel.org/ ... /syslinux](https://kernel.org/pub/linux/utils/boot/syslinux/)