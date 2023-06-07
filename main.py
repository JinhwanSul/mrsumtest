import os
import torch
import argparse

from model.configs import Config
from torch.utils.data import DataLoader
from model.mrsum_dataset import MrSumDataset, BatchCollator
from model.solver import Solver
from data_loader import get_loader


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type = str, default = 'MLP', help = 'the name of the model')
    parser.add_argument('--epochs', type = int, default = 50, help = 'the number of training epochs')
    parser.add_argument('--lr', type = float, default = 0.001, help = 'the learning rate')
    parser.add_argument('--l2_reg', type = float, default = 1e-4, help = 'l2 regularizer')
    parser.add_argument('--dropout_ratio', type = float, default = 0.5, help = 'the dropout ratio')
    parser.add_argument('--batch_size', type = int, default = 256, help = 'the batch size')
    parser.add_argument('--tag', type = str, default = 'dev', help = 'A tag for experiments')

    opt = parser.parse_args()

    kwargs = vars(opt)
    config = Config(**kwargs)

    train_dataset = MrSumDataset('train')
    val_dataset = MrSumDataset('val')
    test_dataset = MrSumDataset('test')

    train_loader = DataLoader(train_dataset, batch_size=opt.batch_size, shuffle=True, num_workers=4, collate_fn=BatchCollator())
    val_loader = DataLoader(val_dataset, batch_size=1, shuffle=False, num_workers=4)
    test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False, num_workers=4)

    solver = Solver(config, train_loader, val_loader, test_loader)

    solver.build()
    test_model_ckpt_path = None

    if config.train:
        best_model_path = solver.train()
        test_model_ckpt_path = best_model_path
    
    if config.test:
        solver.test(test_model_ckpt_path)

# tensorboard --logdir '../PGL-SUM/Summaries/PGL-SUM/'
