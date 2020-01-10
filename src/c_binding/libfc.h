/*
 * Copyright (C) 2016 Red Hat, Inc.
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; If not, see <http://www.gnu.org/licenses/>.
 *
 * Author: Gris Ge <fge@redhat.com>
 */

#ifndef _LIBFC_H_
#define _LIBFC_H_

#include <stdint.h>
#include "libstoragemgmt/libstoragemgmt_common.h"

/*
 * Retrieve FC host speed via /sys/class/fc_host/host<host_no>/speed
 * Preconditions:
 *  err_msg != NULL
 *  link_speed != NULL
 * Return:
 *  LSM_ERR_OK or other LSM error code.
 */
LSM_DLL_LOCAL int _fc_host_speed_get(char *err_msg, unsigned int host_no,
                                     uint32_t *link_speed);

#endif  /* End of _LIBFC_H_ */
