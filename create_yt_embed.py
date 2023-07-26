import subprocess

def get_clipbaord() -> str:
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data.decode("utf-8") 

yt_link: str = get_clipbaord().split("=")[1].split("&")[0]
embed = f"""<iframe width="560" height="315" src="https://www.youtube.com/embed/{yt_link}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>"""
print(embed)