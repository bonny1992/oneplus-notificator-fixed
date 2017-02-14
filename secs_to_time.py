import math
def secs_to_time(seconds):
    if seconds < 60:
        return "{seconds} secondi".format(
        seconds = seconds
        )
    else:
        if int(seconds / 60 / 60 / 24) > 0:
            days = seconds / 60 / 60 / 24
            return "{days} giorni, {hours} ore, {minutes} minuti, {seconds} secondi".format(
            days = int(days),
            hours = int((math.ceil((days - int(days)) * 24))),
            minutes = int((math.ceil((days - int(days)) * 24 * 60))),
            seconds = int(math.ceil((days - int(days)) * 24 * 60 * 60))
            )
        elif int(seconds / 60 / 60) > 0:
            hours = seconds / 60 / 60
            return "{hours} ore, {minutes} minuti, {seconds} secondi".format(
            hours = int(hours),
            minutes = int((math.ceil((hours - int(hours)) * 60))),
            seconds = int((math.ceil((hours - int(hours)) * 60 * 60)))
            )
        elif int(seconds / 60) > 0:
            minutes = seconds / 60
            return "{minutes} minuti, {seconds} secondi".format(
            minutes = int(minutes),
            seconds = int(((minutes - int(minutes)) * 60 ))
            )


print (secs_to_time(300))
