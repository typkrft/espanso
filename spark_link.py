import subprocess

def get_clipbaord() -> str:
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data.decode("utf-8") 

# def set_clipboard(data: str) -> None:
#     p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
#     p.stdin.write(data)
#     p.stdin.close()
#     retcode = p.wait()

def main() -> None:
    url: str = get_clipbaord().removeprefix("https://app.sparkmailapp.com/")
    spark_link: str = f"spark-mail-url:///{url}"
    print(spark_link)

main()
