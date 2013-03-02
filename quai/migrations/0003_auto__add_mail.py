# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mail'
        db.create_table('quai_mail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quai.Person'])),
        ))
        db.send_create_signal('quai', ['Mail'])


    def backwards(self, orm):
        # Deleting model 'Mail'
        db.delete_table('quai_mail')


    models = {
        'quai.mail': {
            'Meta': {'object_name': 'Mail'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quai.Person']"})
        },
        'quai.meet': {
            'Meta': {'object_name': 'Meet'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quai.Person']"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'quai.person': {
            'Meta': {'object_name': 'Person'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_recontacting_loop': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_called': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['quai']