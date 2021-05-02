# emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
def unique_email_add(emails):
    uni_emails = []
    for i in emails:
        local_name = ''
        i_list = i.split('@')
        # i_list[0] = local name
        # i_list[1] = domain name
        for i in i_list[0]:
            if i == '.':
                continue
            if i == '+':
                break
            local_name += i
        full_email = local_name + '@' + i_list[1]

        if full_email not in uni_emails:
            uni_emails.append(full_email)
    return uni_emails

emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]

print(unique_email_add(emails))