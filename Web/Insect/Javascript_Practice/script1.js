function factorial_loop(num) {
    let sum = 1;

    if (num == 0) {
        sum = 0;
        return sum;
    } else if (num == 1) {
        return sum;
    } else if (num < 0) {
        return "Can't understand English?";
    } else if (num % 1 != 0) {
        return "Can't understand English?";
    } else {
        for (let i = 1; i <= num; i++) {
            sum *= i;
        }

        return sum;
    }
}

function loop_work() {
    let loop_inp_value = document.getElementById("loop").value;

    let loop_fac = factorial_loop(loop_inp_value);

    document.getElementById("loop_fac_ans").innerText =
        "Answer：" + loop_fac.toString();
}
