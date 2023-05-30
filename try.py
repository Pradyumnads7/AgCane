from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/AgCane')
def process_data():
    a = request.args.get('a')
    a = eval(a)  # Convert string to dictionary
    df = pd.DataFrame.from_dict(a, orient="index", columns=["value"])
    df.index = pd.to_datetime(df.index)
    df_monthly = df.resample("10D").mean()
    df_monthly = df_monthly.interpolate(method="linear")
    output_dict = df_monthly.to_dict()["value"]

    # Convert Timestamp keys to strings
    # output_dict = {str(key): value for key, value in output_dict.items()}

    # return jsonify(output_dict)

    output_dict = {str(index + 1): value for index, value in enumerate(output_dict.values())}
    print(output_dict)
    return jsonify(output_dict)


if __name__ == '__main__':
    app.run()
