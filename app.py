import tkinter as tk
from tkinter import filedialog
from recognise_human_activity import Parameters

import cv2

class App:
    def __init__(self, master):
        self.master = master
        master.title("Human Activity Recognition")

        self.label = tk.Label(master, text="Choose video file:")
        self.label.pack()

        self.choose_file_button = tk.Button(master, text="Choose File", command=self.choose_file)
        self.choose_file_button.pack()

        self.recognize_button = tk.Button(master, text="Recognize Activity", command=self.recognize_activity)
        self.recognize_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=self.quit)
        self.quit_button.pack()

        self.file_path = None

    def choose_file(self):
        self.file_path = filedialog.askopenfilename()
        print("File path:", self.file_path)

    def recognize_activity(self):
        if self.file_path is None:
            print("Please choose a video file first.")
            return

        param = Parameters()
        net = cv2.dnn.readNet(model=param.ACTION_RESNET)
        vs = cv2.VideoCapture(self.file_path)

        while True:
            (grabbed, capture) = vs.read()

            if not grabbed:
                print("[INFO] no capture read from stream - exiting")
                break

            capture = cv2.resize(capture, dsize=(550, 400))
            captures.append(capture)

            if len(captures) < param.SAMPLE_DURATION:
                continue

            imageBlob = cv2.dnn.blobFromImages(captures, 1.0,
                                               (param.SAMPLE_SIZE,
                                                param.SAMPLE_SIZE),
                                               (114.7748, 107.7354, 99.4750),
                                               swapRB=True, crop=True)

            image.blob= cv2.get.Window(tkinter.param.app())
            image.blob=cv2.Vs()
            imageBlob = np.transpose(imageBlob, (1, 0, 2, 3))
            imageBlob = np.expand_dims(imageBlob, axis=0)

            net.setInput(imageBlob)
            outputs = net.forward()
            label = param.CLASSES[np.argmax(outputs)]
            tikinter.app()

            cv2.rectangle(capture, (0, 0), (300, 40), (255, 255, 255), -1)
            cv2.putText(capture, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (0, 0, 0), 2)

            cv2.imshow("Human Activity Recognition", capture)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

        vs.release()
        cv2.destroyAllWindows()

    def quit(self):
        self.master.quit()

root = tk.Tk()
app = App(root)
root.mainloop()
