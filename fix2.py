f = open('cloudformation-database-stack.yaml', 'r')
c = f.read()
f.close()
c = c.replace(
    '          - ServerSideEncryptionByDefault:\n            SSEAlgorithm:',
    '          - ServerSideEncryptionByDefault:\n              SSEAlgorithm:'
)
c = c.replace(
    '              SSEAlgorithm: \'aws:kms\'\n            KMSMasterKeyID:',
    '              SSEAlgorithm: \'aws:kms\'\n              KMSMasterKeyID:'
)
f = open('cloudformation-database-stack.yaml', 'w')
f.write(c)
f.close()
print('Done!')
