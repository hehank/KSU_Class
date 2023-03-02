function factorial_recursive(num, sum) {
    if (num == 0) {
        return sum;
    } else if (num < 0) {
        return "Can't understand English?";
    } else if (num % 1 != 0) {
        return "Can't understand English?";
    }

    return factorial_recursive(num - 1, sum * num);
}

function recu_work() {
    let recu_inp_value = document.getElementById("recursive").value;

    let recu_fac = factorial_recursive(recu_inp_value, 1);

    if (recu_inp_value == 0 && recu_fac == 1) {
        recu_fac = 0;
    }

    document.getElementById("recu_fac_ans").innerText =
        "Answer：" + recu_fac.toString();
}
