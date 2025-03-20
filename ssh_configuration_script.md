enable
configure terminal

! Set a hostname for the router
hostname SSH-Router

! Set up a domain name (required for SSH)
ip domain-name mynetwork.local

! Generate RSA keys for SSH encryption (1024-bit key)
crypto key generate rsa
  modulus 1024

! Create a local user for SSH login
username admin privilege 15 secret StrongPassword123

! Enable SSH on the vty lines
line vty 0 4
  transport input ssh
  login local
  privilege level 15

! Enable SSH version 2 (for better security)
ip ssh version 2

! Set an idle timeout for security
exec-timeout 5 0

! Save configuration
end
write memory
