import subprocess





def PrintLogs():
    commande = "cd /home/drys/Public/imports-magmi/; php console.php normalize-images data/tsl data/tsl_nrm"
    process = subprocess.Popen(commande, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    while True:
        output = process.stdout.readline().decode().strip()
        error = process.stderr.readline().decode().strip()

        if output == '' and error == '' and process.poll() is not None:
            break

        if output:
            print(output)
        if error:
            print(error)

    process.wait()


PrintLogs()