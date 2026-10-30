#include <opencv2/core.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/tracking.hpp>
#include <sstream>


#include <iostream>

int main() {
    cv::VideoCapture camera(2);

    if (!camera.isOpened()) {
        std::cerr << "Error: Cannot open webcam.\n";
        return -1;
    }

    cv::Mat frame;
    camera >> frame;

    if (frame.empty()) {
        std::cerr << "Error: Cannot read webcam frame.\n";
        return -1;
    }

    cv::Rect roi = cv::selectROI("Select Object", frame, false);

    if (roi.width <= 0 || roi.height <= 0) {
        std::cout << "No object selected.\n";
        return 0;
    }

    cv::Ptr<cv::TrackerCSRT> tracker = cv::TrackerCSRT::create();
    tracker->init(frame, roi);

    std::cout << "Tracking started!\n";
    cv::destroyWindow("Select Object");

    while (true) {
        camera >> frame;
        if (frame.empty()) {
            break;
        }

        bool success = tracker->update(frame, roi);

        cv::rectangle(frame, roi, cv::Scalar(0, 255, 0), 2);
        cv::putText(frame, "Tracker: CSRT", cv::Point(75, 50), cv::FONT_HERSHEY_SIMPLEX, 0.7, cv::Scalar(0, 255, 0), 2);

        std::ostringstream oss;
        oss << "(" << roi.x << ", " << roi.y << ")";

        cv::putText(frame, oss.str(), cv::Point(75, 75), cv::FONT_HERSHEY_SIMPLEX, 0.7, cv::Scalar(0, 255, 0), 2);

        cv::imshow("Live Camera Feed", frame);

        // macOS Virtual Key Code 12 = Q
        if ((cv::waitKey(1) & 0xFF) == 'q') {
            break;
        }
    }

    camera.release();
    cv::destroyAllWindows();

    return 0;
}
