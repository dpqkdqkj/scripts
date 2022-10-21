def to_seconds(hours, minutes, seconds):
    return hours*60*60 + minutes*60 + seconds

def get_total_start_end(hs, ms, ss, he, me, se):
    return to_seconds(hs, ms, ss), to_seconds(he, me, se)

def main():
    ffmpeg_af = "-af \""
    rinput = input()  # f.e.: >>> 3 44 55 3 46 55
    while rinput != "q":
        map_input = map(int, rinput.split(' '))
        start_total, end_total = get_total_start_end(*map_input)
        ffmpeg_af += f"volume=enable='between(t,{start_total},{end_total})':volume=0, "
        rinput = input()
    ffmpeg_af = f"{ffmpeg_af[:-2]}\""
    print(ffmpeg_af)
    

if __name__ == "__main__":
    main()
