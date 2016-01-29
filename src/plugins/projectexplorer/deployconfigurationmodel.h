/****************************************************************************
**
** Copyright (C) 2016 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of Qt Creator.
**
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 3 as published by the Free Software
** Foundation with exceptions as appearing in the file LICENSE.GPL3-EXCEPT
** included in the packaging of this file. Please review the following
** information to ensure the GNU General Public License requirements will
** be met: https://www.gnu.org/licenses/gpl-3.0.html.
**
****************************************************************************/

#ifndef PROJECTEXPLORER_DEPLOYCONFIGURATIONMODEL_H
#define PROJECTEXPLORER_DEPLOYCONFIGURATIONMODEL_H

#include <QAbstractItemModel>

namespace ProjectExplorer {

class Target;
class DeployConfiguration;

// Documentation inside.
class DeployConfigurationModel : public QAbstractListModel
{
    Q_OBJECT
public:
    explicit DeployConfigurationModel(Target *target, QObject *parent = 0);

    int rowCount(const QModelIndex &parent = QModelIndex()) const;
    int columnCount(const QModelIndex &parent = QModelIndex()) const;
    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const;

    DeployConfiguration *deployConfigurationAt(int i);
    DeployConfiguration *deployConfigurationFor(const QModelIndex &idx);
    QModelIndex indexFor(DeployConfiguration *rc);
private:
    void addedDeployConfiguration(ProjectExplorer::DeployConfiguration*);
    void removedDeployConfiguration(ProjectExplorer::DeployConfiguration*);
    void displayNameChanged();
    Target *m_target;
    QList<DeployConfiguration *> m_deployConfigurations;
};

} // namespace ProjectExplorer

#endif // PROJECTEXPLORER_DEPLOYCONFIGURATIONMODEL_H
