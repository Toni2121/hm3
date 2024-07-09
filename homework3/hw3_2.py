test_grade: int = int(input("please enter the grade you got in the last test: "));
if 0 <= test_grade <= 40:
    print("try harder next time...");
elif 41 <= test_grade <= 60:
    print("you're getting there, need some more work");
elif 61 <= test_grade <= 80:
    print("pretty good!");
elif 81 <= test_grade <= 95:
    print("awesome!");
elif 96 <= test_grade <= 100:
    print("excellent!!! You're a Star!");
else:
    print("grade illegal");