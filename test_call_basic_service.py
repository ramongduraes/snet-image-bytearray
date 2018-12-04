if __name__ == "__main__":

    try:
        # Service ONE - Arithmetic
        endpoint = input("Endpoint (localhost:{}): ".format(registry["basic_service_one"]["grpc"]))
        if endpoint == "":
            endpoint = "localhost:{}".format(registry["basic_service_one"]["grpc"])

        # Open a gRPC channel
        channel = grpc.insecure_channel("{}".format(endpoint))

        grpc_method = input("Method (add|sub|mul|div): ")
        a = float(input("Number 1: "))
        b = float(input("Number 2: "))

        if grpc_method == "add":
            stub = grpc_bt_grpc.AdditionStub(channel)
            number = grpc_bt_pb2.Numbers(a=a, b=b)
            response = stub.add(number)
            print(response.value)
        else:
            print("Invalid method!")

    except Exception as e:
        print(e)
