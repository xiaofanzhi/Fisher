from werkzeug.security import generate_password_hash


p1 = generate_password_hash(str(1))

print(p1)

# p1的结果为：pbkdf2:sha256:50000$VZqh6nBQ$8771837aa12266b88e0c2f6300f6c21407fff64cec4f7eec061b24eacabdf7ba



from werkzeug.security import check_password_hash

print(check_password_hash(p1, str(1)))


print(check_password_hash(p1, 'lance1'))

