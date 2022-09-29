
import grpc

target = 'localhost:11526'
vendorChannel = grpc.insecure_channel(target)
