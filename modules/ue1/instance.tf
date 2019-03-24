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