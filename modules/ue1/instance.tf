resource "google_compute_instance" "vm1" {
    name          = "k8s-master"
    machine_type  = "n1-standard-2"
    zone          = "${format("%s","${var.var_region_name}-c")}"

    tags          = ["ssh","http"]

    boot_disk {
        initialize_params {
            image = "centos-7-v20180129"
        }
    }

    metadata {
        foo = "bar"
    }

    network_interface {
        subnetwork = "${google_compute_subnetwork.public_subnet.name}"

        access_config {
            // Ephemeral IP
        }
    }

    provisioner "remote-exec" {
        inline = [
            "sudo -i",
            "yum install -y https://centos7.iuscommunity.org/ius-release.rpm",
            "yum update",
            "yum install -y python36u python36u-libs python36u-devel python36u-pip",
            "python3.6 -V"
        ]

        connection {
            host        = "${self.network_interface.0.access_config.0.nat_ip}"
            type        = "ssh"
            user        = "${var.ssh_user}"
            private_key = "${file("~/.ssh/id_rsa")}"
            # private_key = "${var.ssh_key_private}"
        }
    }

    provisioner "local-exec" {
        environment {
            PUBLIC_IP  = "${self.network_interface.0.access_config.0.nat_ip}"
            # PRIVATE_IP = "${self.ipv4_address_private}"
        }

        working_dir = "../../../ansible/"
        command     = "ansible-playbook -u root --private-key ${var.ssh_key_private} k8s-master.yaml -i ${self.network_interface.0.access_config.0.nat_ip},"
        # command     = "ansible-playbook -u root --private-key "${file("~/.ssh/id_rsa")}" k8s-master.yaml -i ${self.ipv4_address},"
    }
}

resource "google_compute_instance" "vm2" {
    name          = "k8s-node1"
    machine_type  = "n1-standard-1"
    zone          = "${format("%s","${var.var_region_name}-c")}"

    tags          = ["ssh","http"]

    boot_disk {
        initialize_params {
            image = "centos-7-v20180129"
        }
    }

    metadata {
        foo = "bar"
    }

    network_interface {
        subnetwork = "${google_compute_subnetwork.public_subnet.name}"

        access_config {
            // Ephemeral IP
        }
    }
}

resource "google_compute_instance" "vm3" {
    name          = "k8s-node2"
    machine_type  = "n1-standard-1"
    zone          = "${format("%s","${var.var_region_name}-c")}"

    tags          = ["ssh","http"]

    boot_disk {
        initialize_params {
            image = "centos-7-v20180129"
        }
    }

    metadata {
        foo = "bar"
    }

    network_interface {
        subnetwork = "${google_compute_subnetwork.public_subnet.name}"

        access_config {
            // Ephemeral IP
        }
    }
}

resource "google_compute_instance" "vm4" {
    name          = "k8s-node3"
    machine_type  = "n1-standard-1"
    zone          = "${format("%s","${var.var_region_name}-c")}"

    tags          = ["ssh","http"]

    boot_disk {
        initialize_params {
            image = "centos-7-v20180129"
        }
    }

    metadata {
        foo = "bar"
    }

    network_interface {
        subnetwork = "${google_compute_subnetwork.public_subnet.name}"

        access_config {
            // Ephemeral IP
        }
    }
}