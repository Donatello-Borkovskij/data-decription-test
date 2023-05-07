import base64

# def decode_battery_data(encoded_data):

# class Battery:
def decode_battery_data():
    # decoded_bytes = base64.decode(encoded_data)
    decoded_bytes = "4FD45A51D45AC3555C7E155CB6F45A98C563C06559D40597"

    hex_array = []
    for i in range(8):
        col = []
        step = 0
        i *= 6

        for j in range(3):
            col.append(decoded_bytes[i + j + step] + decoded_bytes[i + j + step + 1])
            step += 1

        hex_array.append(col)

    for row in hex_array:
        x = row[0]
        row[0] = row[2]
        row[2] = x

    print(hex_array)
    print(convert_data_to_decimal(hex_array))
    return hex_array


def convert_data_to_decimal(data):
    for x in data:
        index = data.index(x)
        x = x[0]+x[1]+x[2]
        x1 = x[0]+x[1]+x[2]
        x2 = x[3]+x[4]+x[5]
        # x = {int(x1, base=16) * 22.85, int(x2, base=16) * 3.772}
        x = [int(x1, base=16), int(x2, base=16)]
        # print(str(x1) + " " + str(x2))
        # print(x)
        data[index] = x

    data_dict = {
        "0-2": data[0],
        "3-5": data[1],
        "6-8": data[2],
        "9-11": data[3],
        "12-14": data[4],
        "15-17": data[5],
        "21-23": data[6]
    }

    return data_dict


if __name__ == "__main__":
    decode_battery_data()
